#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   AtcGenTemplate.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/2/3 11:24    
@Author     :   liushuliang
@Version    :   1.0
@Description:   生成atc的 go/rust 模板
"""
import os
import sys

from tools.gen_code_tool.AtcCaseSpider import AtcCaseSpider
from tools.gen_code_tool.BaseGenTemplate import BaseGenTemplate


class AtcGenTemplate(BaseGenTemplate):
    def __init__(self, problem_url='https://atcoder.jp/contests/arc119/tasks/arc119_c'):
        super().__init__(problem_url)
        self.url = problem_url
        self.site_tag = 'atc'

        parts = problem_url.split('/')
        self.contest = parts[-3]  # arc148
        self.zip_contest = self.contest  # 由于cf比赛场次有几千，放到一个目录太多了，所以每100场比赛压一个文件夹
        contest = parts[-3]
        for i in range(len(contest)):
            if contest[i:].isdigit():
                c = int(contest[i:])  # 场次划到那个100
                self.zip_contest = f'{contest[:i]}{c//100*100}_{c//100*100+99}'
                break
        self.task_id = parts[-1].split('_')[1] if '_' in parts[-1] else parts[-1][-1]  # c
        self.file_name = parts[-1]  # atc148_c
        self.spider = AtcCaseSpider


if __name__ == '__main__':
    url = 'https://atcoder.jp/contests/abc222/tasks/abc222_f'
    AtcGenTemplate(url).run()
