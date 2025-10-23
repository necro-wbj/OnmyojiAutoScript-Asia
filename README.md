<div align="center">

# OnmyojiAutoScript-Asia (OASA)

## 由 OAS（陸服）分支並適配為 **亞洲服** 版本  
> 搬運 & 持續完善中，歡迎一同建設

<br>

<div>
 <img alt="python" src="https://img.shields.io/badge/python-3.10-%233776AB?logo=python">
</div>
<div>
 <img alt="platform" src="https://img.shields.io/badge/platform-Windows-blueviolet">
</div>
<div>
 <img alt="license" src="https://img.shields.io/github/license/necro-wbj/OnmyojiAutoScript-Asia">
 <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/necro-wbj/OnmyojiAutoScript-Asia">
 <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/necro-wbj/OnmyojiAutoScript-Asia/total">
 <img alt="stars" src="https://img.shields.io/github/stars/necro-wbj/OnmyojiAutoScript-Asia?style=social">
</div>

<br>

陰陽師自動化腳本（亞洲服）  
一鍵託管，解放雙手

#### 主庫: [https://github.com/necro-wbj/OnmyojiAutoScript-Asia](https://github.com/necro-wbj/OnmyojiAutoScript-Asia)

</div>

> 陰陽師已步入生命週期後期。請把重複日常交給 **OASA**，把時間留給更重要的事。

---

## 為何有 OASA？
- 本專案以 **OAS（OnmyojiAutoScript, 陸服）** 為上游，針對 **亞洲服** 的界面、文本與活動節奏做適配與調整。
- 若你來自上游，基本用法與文檔一致；如遇亞洲服特有差異，請先看本文的「差異與限制」。

---

## 功能 Features
- **日常任務**：懸賞封印、小貓咪、小雜簽到、金幣妖怪、年獸、花合戰、地鬼、封魔、御魂整理  
- **每週相關**：真蛇、秘聞競速、神秘商店、搜刮商店、鬥技、每週小雜事  
- **陰陽寮**：結界上卡、結界蹭卡、結界突破、寮突破、狩獵戰、集體任務、道館  
- **御魂副本**：八岐大蛇、業原火、日輪之城、永生之海、六道之門  
- **肝帝專屬**：探索、契靈、禦靈、覺醒副本、石距、百鬼夜行  
- **限時活動**：每期爬塔、超鬼王、對弈競猜、花車巡遊、智力答案

### 顯著特點
- **全部任務**：盡可能覆蓋常見玩法，一條龍釋放雙手（有坑就挖，有餅就畫 🤝）  
- **無縫銜接**：時間管理與任務排程優化，寄養/任務無縫切換  
- **裝飾可選**：支援自訂庭院與主題，[詳細說明](https://github.com/runhey/OnmyojiAutoScript/issues/180)  
- **百鬼夜行**：AI 智慧撒豆，模型含全部式神，[效果展示](https://runhey.github.io/OnmyojiAutoScript-website/docs/user-manual/hyakkiyakou)

---

## 與上游（陸服 OAS）的差異與限制
> 本段會隨適配進度持續更新

- **文字/資產適配**：亞洲服界面文案、資源命名與陸服略有不同，已逐步覆蓋；如遇識別不到或跳轉錯誤，請附截圖回報。  
- **活動節奏**：亞洲服活動檔期常與陸服不同，限時活動支援以「當期實測」為準。  
- **預設配置**：預設伺服區與語系以亞洲服為主；如需跑陸服請回上游。  
- **尚待完善**：少量低頻功能仍在比對修正中，歡迎提交 PR/Issue 協力完善。

### 🛠 實現邏輯的調整與優化（摘錄）
> 為了更貼合亞洲服行為與文本差異，**本分支對部分實現邏輯做了修改與優化**（以實際程式碼為準）：
- **畫面識別**：針對亞洲服界面元素重新訓練與多語系字串映射，並優化模板匹配/閾值策略以提高穩定度。  
- **點擊流程**：新增關鍵步驟的容錯與重試邏輯（超時/誤跳轉自動回復），減少卡死。  
- **日誌與診斷**：細化執行結果碼與錯誤訊息，便於快速回報與定位問題。  

> 若你有更佳的策略（例如某副本的更穩流程/更快判斷），歡迎 PR 以具體改動為準確依據。

---

## 安裝 Installation
> **環境需求**：Windows、Python **3.10**（或相容 3.10.x）

- 📖 [學會提問](https://runhey.github.io/OnmyojiAutoScript-website/docs/user-manual/scientific-question)：**必看**  
- 🚀 [使用手冊](https://runhey.github.io/OnmyojiAutoScript-website/docs/user-manual/getting-started)：完整入門  
- 🧩 [安裝教學](https://runhey.github.io/OnmyojiAutoScript-website/docs/user-manual/installation)：保母式步驟  
- 🛠️ [開發文件](https://runhey.github.io/OnmyojiAutoScript-website/docs/development/preamble)：入門開發與架構概覽  

> **提示**：文檔以上游為主，但步驟一致。

---

## 回報問題 / 參與貢獻
- 提 Issue 前請先閱讀「學會提問」，並附上：**版本、日誌、螢幕截圖/錄影、可重現步驟**。  
- 問題與需求請在 **Issues**；修正/功能請送 **PR**（小步提交、附測試/截圖更佳）。  
- 歡迎補充 **亞洲服專屬資產**（圖片模板、字串映射、活動流程）。

---

## 許可證 LICENSE
本專案以 **GNU General Public License v3.0** 發佈。

---

## 聲明 Announcement
本軟體開源、免費，僅供學習交流使用。開發者團隊擁有本專案的最終解釋權。使用本軟體產生的所有問題與本專案與開發者團隊無關。  
OASA is a free open source software. **If you paid for OASA from any channel, please refund.**  
OASA 是免費開源軟體，**若你在任何管道付費購買，請立即退款**。

---

## 關於 Alas（上游框架）
OAS 基於碧藍航線腳本 [AzurLaneAutoScript](https://github.com/LmeSzinc/AzurLaneAutoScript)（簡稱 **Alas**）開發，並參考星穹鐵道腳本 [StarRailCopilot](https://github.com/LmeSzinc/StarRailCopilot) 的經驗；在其基礎上進行了：  
- **設計重構**：前後端解耦，架構更通用、維護擴充更容易  
- **全新 GUI**：採用 [Flutter](https://flutter.dev) 構建全平台界面  
- **OCR 升級**：採用 [ppocr-onnx](https://github.com/triwinds/ppocr-onnx)，精度與效能兼顧  
- **資產管理**：建立新的 Assets 系統以管理圖片/文字/點擊等資源  
- **設定檔 pydantic 化**：用 [pydantic](https://github.com/pydantic/pydantic) 更優雅地管理配置

---

## 相關項目 Relative Repositories
- [OAS（陸服版）](https://github.com/runhey/OnmyojiAutoScript/tree/dev)：陰陽師陸服自動化腳本  
- [Alas](https://github.com/LmeSzinc/AzurLaneAutoScript)：碧藍航線自動化腳本  
- [SRC](https://github.com/LmeSzinc/StarRailCopilot)：星穹鐵道腳本（下一代 Alas 框架）  
- [OASX](https://github.com/runhey/OASX)：與 OAS 對接的全平台 GUI  
- [NikkeAutoScript](https://github.com/takagisanmie/NIKKEAutoScript)：勝利女神：NIKKE 自動日常腳本  
- [AAS](https://github.com/TheFunny/ArisuAutoSweeper)：蔚藍檔案自動化腳本  
- [MAA](https://github.com/MaaAssistantArknights/MaaAssistantArknights)：明日方舟小助手  
- [FGO-py](https://github.com/hgjazhgj/FGO-py)：Fate/Grand Order 助手  
- [OAS-website](https://github.com/runhey/OnmyojiAutoScript-website)：OAS 文檔網站（[Docusaurus](https://docusaurus.io/)）  
- [ppocr-onnx](https://github.com/triwinds/ppocr-onnx)：基於 onnxruntime 與 PaddleOCR 的 OCR  
- [gurs](https://github.com/2833844911/gurs)：基於貝賽爾曲線的滑動軌跡模擬

> 相較其他遊戲社群，陰陽師玩家對腳本排斥度較高。無論你是否喜歡 OASA，請**勿在公開網路宣傳**，以保護專案與開發者。

---

### 社群
Discord：<https://discord.gg/zNRdjZNmzZ>
