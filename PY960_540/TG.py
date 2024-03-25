token = '5825823192:AAHXcT0UOunElkJ5RxoKzvAMdTrm_hs46ps'
api_id='5825823192'
api_hash='AAHXcT0UOunElkJ5RxoKzvAMdTrm_hs46ps'
UID = 1068022004

import time
import random, os
from telegram.ext import Updater, CommandHandler


updater = Updater('5825823192:AAHXcT0UOunElkJ5RxoKzvAMdTrm_hs46ps')
dispatcher = updater.dispatcher

def start(update, context):
    updater.message.reply_text("123123123123123")
dispatcher.add_handler(CommandHandler('s',start))
picPath=(r'./pic/EVE2/save/')
OldFile=0
OldFile=0
while 1:

    AllFileList = os.listdir(picPath)
    AllFileList.sort(reverse = True)

    if OldFile == AllFileList[0]:
        # do nothing
        time.sleep(5)
    elif OldFile == AllFileList[1]:
        PicSendPath = picPath+AllFileList[0]
        print(PicSendPath)
        file = open(PicSendPath,'rb')
        dispatcher.bot.send_document(chat_id=UID, document=file) 
        file.close()
        OldFile=AllFileList[0]
    else:
        PicSendPath = picPath+AllFileList[1]
        print(PicSendPath)
        file = open(PicSendPath,'rb')
        dispatcher.bot.send_document(chat_id=UID, document=file) 
        file.close()
        PicSendPath = picPath+AllFileList[0]
        print(PicSendPath)
        file = open(PicSendPath,'rb')
        dispatcher.bot.send_document(chat_id=UID, document=file) 
        file.close()
        OldFile=AllFileList[0]
updater.idle()