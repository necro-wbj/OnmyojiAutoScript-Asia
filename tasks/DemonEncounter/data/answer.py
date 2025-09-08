# This Python file uses the following encoding: utf-8
# @author runhey
# github https://github.com/runhey
import csv
import re
import difflib

from datetime import datetime
from pathlib import Path

from module.logger import logger
import time

def remove_symbols(text):
    return re.sub(r'[^\w\s]', '', text)

class Answer:
    def __init__(self):
        self.data: dict[str, list] = {}
        self.data_options: dict[str, list] = {}
        file = str(Path(__file__).parent / 'data.csv')
        with open(file, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                key = remove_symbols(row[0])
                value = remove_symbols(row[1])
                if key not in self.data:
                    self.data[key] = []
                self.data[key].append(value)
                if value not in self.data_options:
                    self.data_options[value] = []
                self.data_options[value].append(key)

    def _decide_by_question_match_ratio(self, ques: str, ops: list[str]) -> int | None:
        logger.info(f'no same question try match:{ques},{ops}')
        max_ratio = 0
        best_questions = []  # 存題目
        best_answers = []    # 存所有最相似題目的所有答案

        # 1. 找到最相似的題目（可能有多個相同最高分）
        for key in self.data.keys():
            ratio = difflib.SequenceMatcher(None, ques, key).ratio()
            if ratio > max_ratio:
                max_ratio = ratio
                best_questions = [key]  # 有更高的，清空再加
                best_answers = self.data[key].copy()  # 直接複製這個題目的答案
            elif ratio == max_ratio:
                best_questions.append(key)  # 一樣高的，繼續加
                best_answers.extend(self.data[key])  # 把這個題目的答案也加進來

        if not best_questions:
            return None
        
        logger.info(f'best_questions:{best_questions}')

        # 2. 用所有最相似題目的答案，和ops比對
        best_score = 0
        best_index = []
        for idx, op in enumerate(ops):
            for ans in best_answers:
                score = difflib.SequenceMatcher(None, op, ans).ratio()
                if score > best_score:
                    best_score = score
                    best_index = [idx]
                elif score == best_score:
                    best_index.append(idx)

        logger.info(f'best_ans:{best_answers}, best_index:{best_index}')

        if best_index:
            return best_index[0] + 1
        return None

    def answer_one(self, question: str, options: list[str]) -> int|None:
        """

        每一个问题有三个选项， 返回选项的序号(1、2、3)
        :param question:
        :param options:
        :return:
        """
        question = remove_symbols(question)
        options = [remove_symbols(op) for op in options]
        logger.info(f'question:{question},options:{options}')
        # 如果答案有 其餘選項皆對 直接選
        if '其餘選項皆對' in options:
            return options.index('其餘選項皆對') + 1
        return self._decide_by_question_match_ratio(question, options)

if __name__ == "__main__":
    answer = Answer()
    question = '冥界中谁拥阁魔之目一双审善度恶'
    options = ['判官', '孟婆', '荒川之主', '阁魔']
    start_time = datetime.now()
    print(answer.answer_one(question, options))
    print(datetime.now() - start_time)