#!/usr/bin/env bash
set -euo pipefail

# ====== 可調參數 ======
UPSTREAM_BRANCH="dev"             # 上游分支（資訊用）
BASE_BRANCH="main"                # 目標 base
PR_BRANCH="sync/upstream-dev"     # PR 分支（你的同步分支）
PYTHON_BIN="python"               # 你的 Python 指令：python / py / py -3 等
# =====================

log() { printf '[LOG] %s\n' "$*"; }
warn() { printf '::warning::%s\n' "$*"; }
err() { printf '::error::%s\n' "$*"; }

# 1) 取回最新、切到 PR 分支
git fetch origin +refs/heads/*:refs/remotes/origin/* --prune
git checkout -B "$PR_BRANCH" "origin/$PR_BRANCH" 2>/dev/null || {
  log "origin/$PR_BRANCH 不存在，改用 upstream 初始建立"
  git fetch upstream +refs/heads/*:refs/remotes/upstream/* --prune || true
  git checkout -B "$PR_BRANCH" "upstream/$UPSTREAM_BRANCH"
  git push -u origin "$PR_BRANCH"
}

log "目前分支：$(git symbolic-ref --short HEAD)"

# 2) 將 base 合併進來（不做快轉），觸發潛在衝突
set +e
git merge --no-ff "origin/$BASE_BRANCH"
MERGE_EXIT=$?
set -e

if [[ $MERGE_EXIT -eq 0 ]]; then
  # 沒衝突、直接完成（但仍可能沒有實際變更）
  if git diff --cached --quiet; then
    log "合併乾淨且無變更，直接結束。"
    exit 0
  else
    log "合併乾淨，有變更 → 直接提交並推送。"
    git commit -m "merge: origin/$BASE_BRANCH into $PR_BRANCH"
    git push origin "HEAD:$PR_BRANCH"
    exit 0
  fi
fi

log "偵測到衝突，先自動處理資源檔（ours）…"

# 3) 自動 ours 的資源檔清單（含 assets.py、圖片/音訊/字型與常見 json）
#    注意：這些只在「有衝突」時處理
mapfile -t UFILES < <(git diff --name-only --diff-filter=U || true)

auto_ours_globs=(
  "assets/**"
  "**/assets.py"
  "**/*.png" "**/*.jpg" "**/*.jpeg" "**/*.gif" "**/*.webp"
  "**/*.mp3" "**/*.wav" "**/*.mp4"  "**/*.mov"
  "**/*.ico" "**/*.ttf" "**/*.otf"
  "**/image*.json" "**/ocr*.json" "**/click*.json"
)

shopt -s globstar nullglob
for f in "${UFILES[@]}"; do
  for pat in "${auto_ours_globs[@]}"; do
    # 用 bash 的樣式比對（不使用正則）
    if [[ "$f" == $pat ]]; then
      git checkout --theirs -- "$f" || true
      git add -- "$f" || true
      echo "[KEEP BASE(main)] $f"
      break
    fi
  done
done
shopt -u globstar nullglob

# 4) 生成 assets.py（優先 extra_assets.py，否則退回 assets_extract.py）
GEN_SRC=""
if [[ -f "./extra_assets.py" ]]; then
  GEN_SRC="./extra_assets.py"
  log "使用 extra_assets.py 生成 assets.py"
elif [[ -f "./assets_extract.py" ]]; then
  GEN_SRC="./assets_extract.py"
  log "使用 assets_extract.py 生成 assets.py（備援）"
else
  # 從 base 分支抓生成器（避免分支缺檔）
  log "分支缺少生成器，嘗試從 origin/$BASE_BRANCH 取回"
  git show "origin/$BASE_BRANCH:extra_assets.py" > ./extra_assets_temp.py 2>/dev/null || true
  if [[ -s ./extra_assets_temp.py ]]; then
    GEN_SRC="./extra_assets_temp.py"
    log "臨時使用 origin/$BASE_BRANCH 的 extra_assets.py"
  else
    git show "origin/$BASE_BRANCH:assets_extract.py" > ./assets_extract_temp.py
    GEN_SRC="./assets_extract_temp.py"
    log "臨時使用 origin/$BASE_BRANCH 的 assets_extract.py"
  fi
fi

set +e
PYTHONPATH="$PWD" "$PYTHON_BIN" "$GEN_SRC"
GEN_EXIT=$?
set -e

rm -f ./extra_assets_temp.py ./assets_extract_temp.py || true

# 5) 若生成器失敗且 repo 內沒有任何 assets.py，盡量還原舊版以保持可用
if [[ $GEN_EXIT -ne 0 ]]; then
  warn "生成器執行失敗（exit=$GEN_EXIT）。"
fi

if ! git ls-files --error-unmatch '**/assets.py' >/dev/null 2>&1 && ! ls **/assets.py 1>/dev/null 2>&1; then
  warn "專案內沒有任何 assets.py，被生成器清空了？嘗試還原上一版。"
  git checkout "HEAD~1" -- "**/assets.py" 2>/dev/null || true
  if ! ls **/assets.py 1>/dev/null 2>&1; then
    git show "origin/$BASE_BRANCH:tasks/Component/GeneralBattle/assets.py" > tasks/Component/GeneralBattle/assets.py 2>/dev/null || true
  fi
fi

# 6) 把資產變更（assets.py、assets 資料夾）加到索引
#    注意：只加這些，其他衝突先保留不提交
git add -- **/assets.py 2>/dev/null || true
git add -- assets/**   2>/dev/null || true

# 7) 檢查是否還有衝突檔（通常是 script/config 等程式碼）
if git diff --name-only --diff-filter=U | grep -q .; then
  warn "仍有需手動解決的衝突檔如下："
  git diff --name-only --diff-filter=U | sed 's/^/ - /'
  echo
  echo "請手動編輯上列檔案解衝突後，執行："
  echo "  git add <檔案...>"
  echo "  git commit -m \"merge: origin/$BASE_BRANCH into $PR_BRANCH (assets=ours, regenerated)\""
  echo "  git push origin HEAD:$PR_BRANCH"
  exit 1
fi

# 8) 沒有剩餘衝突 → 提交並推送
if git diff --cached --quiet; then
  log "只有資產檔衝突且都處理，但沒有任何 staged 變更；中止合併並結束。"
  git merge --abort || true
  exit 0
else
  git commit -m "merge: origin/$BASE_BRANCH into $PR_BRANCH (assets=ours, regenerated)"
  git push origin "HEAD:$PR_BRANCH"
  log "完成：已提交並推送。"
fi
