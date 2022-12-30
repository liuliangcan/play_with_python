#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   AtcLocalTest.py    
@License    :   None
@Project    :   NormalTools
@Software   :   PyCharm
@ModifyTime :   2022/11/15 22:13
@Author     :   liushuliang
@Version    :   1.0
@Description:   本地测试的代码主程序不关心，因此可以搞出来
"""
import io
from contextlib import redirect_stdout


class AtcLocalTest:
    def __init__(self, main_func, url, test_cases,choose_case=None, spider_switch=True):
        """
        :param main_func:
        :param url: https://atcoder.jp/contests/abc210/tasks/abc210_e
        :param test_cases: 2个字段分别是input和output；仅当SPIDER_SWITCH=False时，才会使用传入的自定义case，否则会在线爬;爬第一次会存本地以后不爬了
        :param spider_switch: 当爬虫开关为True时，会在线爬case，main里设置的case会被覆盖不生效；如果要用本地case需要设置False;
        """
        self.main_func = main_func
        self.spider_switch = spider_switch
        self.url = url
        if type(test_cases) is tuple:
            test_cases = list(test_cases)
        if type(test_cases) is list:
            test_cases = {f'case{i}': v for i, v in enumerate(test_cases)}

        self.choose_case = choose_case
        self.test_cases = test_cases

    def run(self):
        test_cases = self.test_cases
        if self.spider_switch:
            from atc.AtcCaseSpider import AtcCaseSpider
            test_cases = AtcCaseSpider(self.url).save(choose_case=self.choose_case)
        total_result = 'ok!'
        for i, (in_data, result) in test_cases.items():
            result = result.strip()
            with io.StringIO(in_data.strip()) as buf_in:
                RI = lambda: map(int, buf_in.readline().split())
                RS = lambda: buf_in.readline().strip().split()
                with io.StringIO() as buf_out, redirect_stdout(buf_out):
                    self.main_func(RS, RI)
                    output = buf_out.getvalue().strip()
                if output == result:
                    print(f'{i}: result={result}, output={output}, ---ok!')
                else:
                    print(f'{i}: result={result}, output={output}, ---WA!---WA!---WA!')
                    total_result = '---WA!---WA!---WA!'
        print('\n', total_result)
