# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import csv

from datetime import datetime
from pathlib import Path
from module.logger import logger


def answer_one(question: str, options: list[str]) -> int:
    """

    每一个问题有四个选项， 返回选项的序号(1、2、3)
    :param question:
    :param options:
    :return:
    """
    # file = str(Path(__file__).parent / 'data.csv')
    # with open(file, newline='', encoding='utf-8-sig') as csvfile:
    #     reader = csv.reader(csvfile)
    #     next(reader)
    #     for row in reader:
    #         if row[0] == question:
    #             try:
    #                 return options.index(row[1]) + 1
    #             except ValueError:
    #                 return 1
    #     return 1
    ## 我要重寫上面的代碼 改為找最相似的 而不是完全一樣的
    question_lcut = set(list(str(question)))
    file = str(Path(__file__).parent / 'data.csv')
    with open(file, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        max_score = 0
        max_score_index = 0
        for row in reader:
            # score 為row[0]與question的相似度
            score = 0
            question_row_lcut = set(list(str(row[0])))
            score = len(question_lcut & question_row_lcut) / len(question_lcut | question_row_lcut)
            if score > max_score:
                max_score = score
                max_score_index = row[1]
                logger.info(f"CSV question: {question} ans: {row[0]} score: {score}")
        # here match the answer
        Ans_lcut = set(list(str(row[1])))
        Ans_score = 0
        Ans_score_max = 0
        final_ans = 0
        # check fully match answer exists or use similar answer
        if row[1] in options:
            return options.index(row[1]) + 1
        else:
            for option in options:
                option_lcut = set(list(str(option)))
                Ans_score = len(Ans_lcut & option_lcut) / len(Ans_lcut | option_lcut)
                if Ans_score > Ans_score_max:
                    Ans_score_max = Ans_score
                    final_ans = option
        try:
            #print question and answer
            print(question, final_ans)
            return options.index(final_ans) + 1
        except ValueError:
            return 1
    return 1




if __name__ == "__main__":
    question = '以下式神中，手持折扇的是'
    options = ['生命上限', '鬼王', '荒川之主']
    start_time = datetime.now()
    print(answer_one(question, options))
    print(datetime.now() - start_time)
    print(answer_one(question, options))
