<div align="center">

# OnmyojiAutoScript-Asia

## 搬移過來的庫，歡迎加入一同建立，以下還需完善

<br>

<div>
    <img alt="python" src="https://img.shields.io/badge/python-3.10-%233776AB?logo=python">
</div>
<div>
    <img alt="platform" src="https://img.shields.io/badge/platform-Windows-blueviolet">
</div>
<div>
    <img alt="license" src="https://img.shields.io/github/license/runhey/OnmyojiAutoScript">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/runhey/OnmyojiAutoScript">
    <img alt="GitHub all releases" src="https://img.shields.io/github/downloads/runhey/OnmyojiAutoScript/total">
    <img alt="stars" src="https://img.shields.io/github/stars/runhey/OnmyojiAutoScript?style=social">
</div>
<br>

阴阳师自动化脚本 

一键托管


### [文档](https://runhey.github.io/OnmyojiAutoScript-website/)

#### 主仓库: [https://github.com/necro-wbj/OnmyojiAutoScript-Asia](https://github.com/necro-wbj/OnmyojiAutoScript-Asia)

</div>

阴阳师，作为一个手游，已经进入了生命周期的晚期。从现在到关服的这段时间里，请减少花费在阴阳师上的时间，把一切都交给 OAS。

## 功能 Features

- **日常任务**: 悬赏封印、小猫咪、小杂签到、金币妖怪、年兽、花合战、地鬼、封魔、御魂整理
- **每周相关**: 真蛇、秘闻竞速、神秘商店、搜刮商店、斗技、每周小杂事
- **阴阳寮**: 结界上卡、结界蹭卡、结界突破、寮突破、狩猎战、集体任务、道馆
- **御魂副本**: 八岐大蛇、业原火、日轮之城、永生之海、六道之门
- **肝帝专属**: 探索、契灵、御灵、觉醒副本、石距、百鬼夜行
- **限时活动**: 每期爬塔、超鬼王、对弈竞猜、花车巡游、智力答题

### 显著特点 
- **全部任务**: 你能想到的没有想到的都有，一条龙给你解放双手（该画饼画饼，该挖坑挖坑）
- **无缝衔接**: 时间管理大师，优异的任务调度系统，无缝寄养，无缝执行任务
- **装饰可选**: 全部初始皮肤是什么鬼，这里支持你喜欢的庭院、主题等等，[详细说明](https://github.com/runhey/OnmyojiAutoScript/issues/180)
- **百鬼夜行**: 利用AI来智能撒豆子，模型包含所有式神，[效果展示](https://runhey.github.io/OnmyojiAutoScript-website/docs/user-manual/hyakkiyakou)

## 许可证 LICENSE

This project is licensed under the GNU General Public License v3.0.

## 声明 Announcement
本软件开源、免费，仅供学习交流使用。开发者团队拥有本项目的最终解释权。使用本软件产生的所有问题与本项目与开发者团队无关。
OAS is a free open source software, if you paid for OAS from any channel, please refund.
OAS 是一款免费开源软件，如果你在任何渠道付费购买了OAS，请退款。

## 关于 Alas
OAS 基于碧蓝航线脚本 [AzurLaneAutoScript](https://github.com/LmeSzinc/AzurLaneAutoScript) 开发，考虑到星穹铁道脚本 [StarRailCopilot](https://github.com/LmeSzinc/StarRailCopilot) 中所提及的问题，
OAS 在其基础上进行了如下优化：
- **调整设计架构**: 将前后端拆离出来更加灵活，方便后续的维护和扩展；优化代码架构使其减少同游戏耦合，更加通用。
- **搭建新的GUI**: 原先的方案过于臃肿，选用 [flutter](https://flutter.cn) 搭建一个全平台的界面端，界面更加舒适简洁
- **新的OCR库**: 跟随 [LmeSzinc](https://github.com/LmeSzinc) 的步伐， [ppocr-onnx](https://github.com/triwinds/ppocr-onnx) 更加简易使用，精度更高速度更快 
- **新的Assets管理**: 构建了一个新的Assets管理系统，更加方便的管理游戏资源如图片，文字，点击等等
- **配置文件 [pydantic](https://github.com/pydantic/pydantic) 化**: pydantic 可以更加优雅的管理用户配置

## 相关项目 Relative Repositories

- [OAS](https://github.com/runhey/OnmyojiAutoScript/tree/dev)陰陽師陸服版本自動化腳本
- [Alas](https://github.com/LmeSzinc/AzurLaneAutoScript): 碧蓝航线的自动化脚本
- [SRC](https://github.com/LmeSzinc/StarRailCopilot): 星铁速溶茶，崩坏：星穹铁道脚本，基于下一代Alas框架。
- [OASX](https://github.com/runhey/OASX): 同 OAS 对接的全平台 GUI
- [NikkeAutoScript](https://github.com/takagisanmie/NIKKEAutoScript): 胜利女神：NIKKE 自动日常脚本
- [AAS](https://github.com/TheFunny/ArisuAutoSweeper): 蔚蓝档案自动化脚本
- [MAA](https://github.com/MaaAssistantArknights/MaaAssistantArknights): 明日方舟小助手，全日常一键长草
- [FGO-py](https://github.com/hgjazhgj/FGO-py): 全自动免配置跨平台开箱即用的Fate/Grand Order助手
- [OAS-website](https://github.com/runhey/OnmyojiAutoScript-website): OAS 的文档网站，使用 [docusaurus](https://docusaurus.io/) 构建
- [ppocr-onnx](https://github.com/triwinds/ppocr-onnx): OCR 库，基于 onnxruntime 和 PaddleOCR
- [gurs](https://github.com/2833844911/gurs): 基于赛贝尔曲线模拟滑动轨迹, 引入其轨迹模拟人手滑动


相對於其他的遊戲，陰陽師玩家整體而言對腳本這類工具具有極高的排斥性。樹大招風，無論你是否喜歡 OAS ，我們都希望你不在互聯網上進行宣傳，這保護 OAS , 也保護開發者們。

#### Discord: https://discord.gg/zNRdjZNmzZ


## 安装 Installation 

- [学会提问](https://runhey.github.io/OnmyojiAutoScript-website/docs/user-manual/scientific-question): 最基本的要求，**必看必学必会**
- [用户手册](https://runhey.github.io/OnmyojiAutoScript-website/docs/user-manual/getting-started): 在线手册，不定期更新，包含所有使用说明
- [安装教程](https://runhey.github.io/OnmyojiAutoScript-website/docs/user-manual/installation): 保姆式安装手册,多翻翻有惊喜
- [开发文档](https://runhey.github.io/OnmyojiAutoScript-website/docs/development/preamble): 虽然迭代很多、年久失修，但入门开发必读，具体以源码为准