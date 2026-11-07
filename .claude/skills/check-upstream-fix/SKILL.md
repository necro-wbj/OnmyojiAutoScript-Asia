---
name: check-upstream-fix
description: 修正任何 bug 或功能問題之前使用。先查原庫 runhey/OnmyojiAutoScript（upstream/dev）是否已修過同一個問題，決定要 cherry-pick、等同步，還是本地暫時修正，並依原庫寫法降低之後的合併衝突。
---

# 修正前先查原庫

本專案是 OAS 陸服的亞服 fork，原庫（`upstream`）更新快、使用者多。修任何問題前先走這個流程，避免另寫一版、之後同步時衝突。

## 1. 取得原庫最新狀態

```bash
git fetch upstream
```

## 2. 查原庫有沒有修過

用問題相關的任務名、模組路徑、資產名稱搜尋本地還沒有的原庫 commit：

```bash
git log --oneline HEAD..upstream/dev -- tasks/<模組>/
git log --oneline HEAD..upstream/dev -i --grep "<關鍵字>"
git diff HEAD...upstream/dev -- tasks/<模組>/
```

必要時也看已同步過、但可能被本地改動蓋掉的部分：`git log --oneline upstream/dev -- <檔案>`。

## 3. 依結果決定做法

| 情況 | 做法 |
|------|------|
| 原庫已修，可直接套用 | `git cherry-pick <commit>`，或等下次同步 |
| 原庫已修，但依賴尚未同步的架構 | 本地暫時修正，**沿用原庫的資產名稱、ROI、檔名與寫法**，讓之後同步可直接採用原庫版本；commit 訊息註明對應的原庫 commit |
| 原庫沒修，問題小、不影響日常使用、原庫近期可能會修 | 可以先不修，等同步 |
| 原庫沒修，且是亞服專屬或影響使用 | 自己修，遵守 CLAUDE.md 的「修改原則」 |

## 4. Commit

- 格式：`fix(模組): 說明`，繁體中文。
- 參考原庫時在內文註明，例如：`對應原庫 commit abc1234`。
