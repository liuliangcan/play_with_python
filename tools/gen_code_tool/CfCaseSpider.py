#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   CfCaseSpider.py
@License    :   None
@Project    :   NormalTools
@Software   :   PyCharm
@ModifyTime :   2023/02/05 20:13
@Author     :   liushuliang
@Version    :   1.0
@Description:   因为c
"""
import os.path
import sys

from collections import defaultdict


class CfCaseSpider:
    """
    爬取cf的case,以字典形式返回: {'case1':(case1_input,case1_output_data), 'case2':(case2_input,case2_output), ...}
    """

    def __init__(self, url):
        """
        初始化
        :param url: https://codeforces.com/problemset/problem/777/D
        """
        self.url = url

    def cases(self):
        """
        :return: {'case1':(case1_input,case1_output_data), 'case2':(case2_input,case2_output), ...}
        """
        import requests
        payload = {}
        headers = {}

        response = requests.request("GET", self.url, headers=headers, data=payload)
        text = response.text
        # print(text)
        from lxml import etree

        html = etree.HTML(text)

        ans = defaultdict(dict)  # case号:{0:input_data,1:output_data}
        # sections = html.xpath(
        #     '/html/body/div/div/div/div/div[@id="task-statement"]/span[@class="lang"]/span[@class="lang-en"]/div/section')
        inputs = html.xpath('/html/body/div/div/div/div/div/div/div/div[@class="sample-test"]/div[@class="input"]')
        # print(sections)
        for i, inp in enumerate(inputs, start=1):
            # print(inp.xpath('./pre/text()'))
            # ['3', '#book', '#bigtown', '#big']
            data = '\n'.join(inp.xpath('./pre/text()'))
            divs = [x for x in inp.xpath('./pre/div/text()')]  # 也有可能是一堆div
            if divs:
                data = '\n'.join(divs)


            ans[f'case{i}'][0] = data.strip().replace('\r\n', '\n')
        outputs = html.xpath('/html/body/div/div/div/div/div/div/div/div[@class="sample-test"]/div[@class="output"]')
        for i, outp in enumerate(outputs, start=1):
            # print(outp.xpath('./pre/text()'))
            data = '\n'.join(outp.xpath('./pre/text()'))
            divs = [x for x in outp.xpath('./pre/div/text()')]
            if divs:
                data = '\n'.join(divs)
            ans[f'case{i}'][1] = data.strip().replace('\r\n', '\n')

        return {k: [v[0], v[1]] for k, v in
                ans.items()}  # 返回cases字典 {'case1':(case1_input,case1_output_data), 'case2':(case2_input,case2_output), ...}


if __name__ == '__main__':
    url = 'https://codeforces.com/problemset/problem/1695/C'
    # url =  'https://codeforces.com/problemset/problem/777/D'
    # print(os.path.basename(url))
    print(CfCaseSpider(url).cases())
    # print(CfCaseSpider(url).cases())
    # for i, (case_input, case_output) in enumerate(CfCaseSpider(url).cases().values(), 1):
    #     print(f'Case {i} input:')
    #     print(case_input.strip())
    #     print(f'Case {i} output:')
    #     print(case_output)
