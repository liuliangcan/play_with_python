#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   CfGenTemplate.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/2/5 20:42
@Author     :   liushuliang
@Version    :   1.0
@Description:   生成cf的 go/rust 模板
"""
import os

from tools.gen_code_tool.BaseGenTemplate import BaseGenTemplate
from tools.gen_code_tool.CfCaseSpider import CfCaseSpider


class CfGenTemplate(BaseGenTemplate):
    def __init__(self, problem_url='https://codeforces.com/problemset/problem/777/D'):
        # https://codeforces.com/problemset/problem/1733/D2

        #https://codeforces.com/contest/1442/problem/A
        super().__init__(problem_url)
        self.url = problem_url
        self.site_tag = 'cf'

        parts = problem_url.split('/')
        contest = parts[-3] if parts[-4] == "contest" else parts[-2]
        self.contest = f'{self.site_tag}{contest}'  # cf777  由于只给777,rust的mod模块会报命名错误，因此命名为cf777
        self.zip_contest = self.contest  # 由于cf比赛场次有几千，放到一个目录太多了，所以每100场比赛压一个文件夹
        if contest.isdigit():
            c = int(contest)  # 场次划到那个100
            self.zip_contest = f'{self.site_tag}{c//100*100}_{c//100*100+99}'
        self.task_id = parts[-1].lower()  # d/d2 由于rust大写会报警告，这里统一转小写
        self.file_name = f"{self.contest}{self.task_id}"  # cf777D
        self.spider = CfCaseSpider


if __name__ == '__main__':
    url = 'https://codeforces.com/problemset/problem/777/D'
    CfGenTemplate(url).run()
