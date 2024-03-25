import logging

# 設定logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def log(msg):
    # 輸出到檔案
    logging.info(msg)
    # 輸出到螢幕
    print(msg)