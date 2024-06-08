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
    question_lcut = set(list(str(question)))
    logger.info(f'OCR Question: {question}, Answer: {options}')
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
            if score >= max_score:
                max_score = score
                max_score_index = row[1]
                logger.info(f"CSV question: {row[0]} ans: {row[1]} better")
                #TODO: handle same score EX :who has brother or sister? 
        # here match the answer
        logger.info(f"final ans={max_score_index}")
        Ans_lcut = set(list(str(max_score_index)))
        Ans_score = 0
        Ans_score_max = 0
        final_ans = 0
        # check fully match answer exists or use similar answer
        if max_score_index in options:
            logger.info(f"Ans: {max_score_index} fully match")
            return options.index(max_score_index) + 1
        else:
            for option in options:
                logger.info(f"matching ans: {option} better")
                option_lcut = set(list(str(option)))
                Ans_score = len(Ans_lcut & option_lcut) / len(Ans_lcut | option_lcut)
                if Ans_score > Ans_score_max:
                    Ans_score_max = Ans_score
                    final_ans = option
        try:
            #print question and answer
            logger.info(f"1Question: {question} Ans: {final_ans}")
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
