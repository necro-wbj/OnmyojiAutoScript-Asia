from module.atom.image import RuleImage
from module.atom.click import RuleClick
from module.atom.long_click import RuleLongClick
from module.atom.swipe import RuleSwipe
from module.atom.ocr import RuleOcr
from module.atom.list import RuleList

# This file was automatically generated by ./dev_tools/assets_extract.py.
# Don't modify it manually.
class RestartAssets: 


	# Image Rule Assets
	# 点击勾玉 
	I_HARVEST_JADE = RuleImage(roi_front=(732,489,34,33), roi_back=(177,451,973,141), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_jade.png")
	# 签到小图标 
	I_HARVEST_SIGN = RuleImage(roi_front=(253,504,24,27), roi_back=(70,471,889,89), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign.png")
	# description 
	I_HARVEST_SIGN_2 = RuleImage(roi_front=(592,135,100,252), roi_back=(592,135,100,252), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_2.png")
	# 999签到福袋 
	I_HARVEST_SIGN_999 = RuleImage(roi_front=(345,494,23,29), roi_back=(51,459,888,103), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_999.png")
	# 邮件小图标 
	I_HARVEST_MAIL = RuleImage(roi_front=(337,505,37,25), roi_back=(38,465,880,89), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail.png")
	# 全部收取 
	I_HARVEST_MAIL_ALL = RuleImage(roi_front=(80,622,75,64), roi_back=(80,622,75,64), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_all.png")
	# 有些邮件需要点击一次 
	I_HARVEST_MAIL_OPEN = RuleImage(roi_front=(163,367,45,48), roi_back=(139,86,100,487), threshold=0.9, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_open.png")
	# 确认收取邮件 
	I_HARVEST_MAIL_CONFIRM = RuleImage(roi_front=(687,543,168,64), roi_back=(687,543,168,64), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_confirm.png")
	# description 
	I_HARVEST_SOUL = RuleImage(roi_front=(241,497,38,36), roi_back=(68,480,930,72), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul.png")
	# description 
	I_HARVEST_MAIL_TITLE = RuleImage(roi_front=(520,48,245,41), roi_back=(520,48,245,41), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_mail_title.png")
	# description 
	I_HARVEST_AP = RuleImage(roi_front=(721,486,31,38), roi_back=(206,462,970,134), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_ap.png")
	# 打开聊天频道会自动关闭 
	I_HARVEST_CHAT_CLOSE = RuleImage(roi_front=(639,309,35,100), roi_back=(639,309,35,100), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_chat_close.png")
	# 签到 
	I_HARVEST_SIGN_3 = RuleImage(roi_front=(291,495,33,36), roi_back=(100,473,1014,91), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_3.png")
	# description 
	I_HARVEST_SIGN_4 = RuleImage(roi_front=(587,151,100,228), roi_back=(547,123,185,281), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_sign_4.png")
	# 点击随机御魂 
	I_HARVEST_SOUL_1 = RuleImage(roi_front=(248,501,34,37), roi_back=(165,389,929,168), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul_1.png")
	# 选择第一个御魂 
	I_HARVEST_SOUL_2 = RuleImage(roi_front=(586,561,112,47), roi_back=(570,547,139,71), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul_2.png")
	# description 
	I_HARVEST_SOUL_3 = RuleImage(roi_front=(313,489,188,33), roi_back=(302,472,216,60), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_soul_3.png")
	# 寮包 
	I_HARVEST_GUILD_REWARD = RuleImage(roi_front=(244,498,41,42), roi_back=(200,403,817,157), threshold=0.8, method="Template matching", file="./tasks/Restart/harvest/harvest_harvest_guild_reward.png")


	# Image Rule Assets
	# 庭院卷轴打开 
	I_LOGIN_SCROOLL_OPEN = RuleImage(roi_front=(1208,609,33,83), roi_back=(1208,609,33,83), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_scrooll_open.png")
	# 庭院卷轴关闭 
	I_LOGIN_SCROOLL_CLOSE = RuleImage(roi_front=(1181,634,28,39), roi_back=(1162,595,77,112), threshold=0.7, method="Template matching", file="./tasks/Restart/login/login_login_scrooll_close.png")
	# description 
	I_LOGIN_RED_CLOSE = RuleImage(roi_front=(1158,62,39,37), roi_back=(912,42,309,281), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_red_close.png")
	# description 
	I_LOGIN_YELLOW_CLOSE = RuleImage(roi_front=(1177,28,46,44), roi_back=(1152,6,94,86), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_yellow_close.png")
	# 用于判断是否出现登录选区的 
	I_LOGIN_8 = RuleImage(roi_front=(178,572,53,60), roi_back=(1,547,241,105), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_8.png")
	# 登录时候不观看CG视频 
	I_WATCH_VIDEO_CANCEL = RuleImage(roi_front=(466,396,130,61), roi_back=(466,396,130,61), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_watch_video_cancel.png")
	# 指定角色进入游戏,默认第一个 
	I_LOGIN_SPECIFIC_SERVE = RuleImage(roi_front=(24,33,52,47), roi_back=(24,33,52,47), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_specific_serve.png")
	# 下载插画 
	I_LOGIN_LOAD_DOWN = RuleImage(roi_front=(725,408,69,32), roi_back=(653,350,232,131), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_load_down.png")
	# description 
	I_LOGIN_FIX = RuleImage(roi_front=(1196,514,60,54), roi_back=(1196,514,60,54), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_fix.png")
	# description 
	I_LOGIN_DOWNLOAD_DRAW = RuleImage(roi_front=(743,459,100,42), roi_back=(651,328,320,241), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_download_draw.png")
	# 同意协议 
	I_LOGIN_CONTRACT_AGREE = RuleImage(roi_front=(535,575,209,62), roi_back=(535,575,209,62), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_contract_agree.png")
	# 請求評論 
	I_LOGIN_COMMENT_REQUEST = RuleImage(roi_front=(535,523,201,42), roi_back=(535,523,201,42), threshold=0.8, method="Template matching", file="./tasks/Restart/login/login_login_comment_request.png")


	# Ocr Rule Assets
	# 正在连接服务器 
	O_LOGIN_NETWORK = RuleOcr(roi=(534,649,189,39), area=(210,492,100,100), mode="Single", method="Default", keyword="正在连接服务器", name="login_network")
	# 進入遊戲 
	O_LOGIN_ENTER_GAME = RuleOcr(roi=(558,573,161,44), area=(545,560,191,73), mode="Single", method="Default", keyword="進入", name="login_enter_game")
	# 点击屏幕跳过 
	O_LOGIN_SKIP_1 = RuleOcr(roi=(1046,35,130,37), area=(1046,35,130,37), mode="Single", method="Default", keyword="点击屏幕跳过", name="login_skip_1")
	# 登录指定角色，默认第一个 
	O_LOGIN_SPECIFIC_SERVE = RuleOcr(roi=(694,605,59,34), area=(516,75,662,585), mode="Single", method="Default", keyword="游戏", name="login_specific_serve")


