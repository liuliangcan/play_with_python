#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   AtcCaseSpider.py    
@License    :   None
@Project    :   NormalTools
@Software   :   PyCharm
@ModifyTime :   2022/11/15 21:33
@Author     :   liushuliang
@Version    :   1.0
@Description:   因为copy case很烦不如爬一下;使用request+xpath提取
                如果本地没有【..../cases/abc210/d】这个目录，会创建然后爬样例；如果存在，就不爬了，直接读
                因此如果要重置本地数据，至少要删除到【d】这一层

                下载abc数据的网址:https://www.dropbox.com/sh/nx3tnilzqz7df8a/AAAYlTq2tiEHl5hsESw6-yfLa?dl=0
                下载后贴到对应的目录下就能用，不会再爬样例。
                from atc.AtcCaseSpider import AtcCaseSpider
                test_cases = AtcCaseSpider(self.url).save()
"""
import os.path
import sys

from collections import defaultdict


class AtcCaseSpider:
    """
    爬取atc的case,以字典形式返回: {'case1':(case1_input,case1_output_data), 'case2':(case2_input,case2_output), ...}
    """

    def __init__(self, url):
        """
        初始化
        :param url: https://atcoder.jp/contests/abc210/tasks/abc210_e
        """
        self.url = url

    def cases(self):
        """
        :return: {'case1':(case1_input,case1_output_data), 'case2':(case2_input,case2_output), ...}
        """
        import requests
        payload = {}
        headers = {}
        print(self.url)
        response = requests.request("GET", self.url, headers=headers, data=payload)
        text = response.text
        # print(text)
        from lxml import etree

        html = etree.HTML(text)
        sections = html.xpath(
            '/html/body/div/div/div/div/div[@id="task-statement"]/span[@class="lang"]/span[@class="lang-en"]/div/section')

        ans = defaultdict(dict)  # case号:{0:input_data,1:output_data}

        for section in sections:
            tag = section.xpath('./h3/text()')
            data = section.xpath('./pre/text()')
            if tag and data and tag[0].startswith('Sample '):
                tag = tag[0].strip().split()
                input_or_out = 0 if tag[1] == 'Input' else 1
                # print(input_or_out)
                # print(tag)
                ans[f'case{tag[2]}'][input_or_out] = data[0].strip().replace('\r\n', '\n')
        # print(ans)
        return {k: [v[0], v[1]] for k, v in
                ans.items()}  # 返回cases字典 {'case1':(case1_input,case1_output_data), 'case2':(case2_input,case2_output), ...}

    def save(self, case_dir=None,choose_case=None):
        if not case_dir:
            match, t = os.path.basename(self.url).split('_')
            case_dir = os.path.join('cases', match, t)
        in_dir = os.path.join(case_dir, 'in')
        out_dir = os.path.join(case_dir, 'out')
        if not os.path.exists(in_dir):
            os.makedirs(in_dir)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
            for i, (case_input, case_output) in AtcCaseSpider(self.url).cases().items():
                case_input_path = os.path.join(in_dir, f'{i}.txt')
                case_output_path = os.path.join(out_dir, f'{i}.txt')

                with open(case_input_path, 'w') as f:
                    f.write(case_input)
                with open(case_output_path, 'w') as f:
                    f.write(case_output)
        ans = {}
        for root, dirs, files in os.walk(in_dir):
            for file in files:
                p = file
                if not choose_case or p in choose_case:
                    case_path = os.path.join(root, file)
                    with open(case_path, 'r') as f:
                        ans[p] = [f.read()]
        for root, dirs, files in os.walk(out_dir):
            for file in files:
                p = file
                if not choose_case or p in choose_case:
                    case_path = os.path.join(root, file)
                    with open(case_path, 'r') as f:
                        ans[p].append(f.read())
        for k, v in ans.items():
            if len(v) != 2:
                sys.stderr.write(f'注意，{k}这组case只有in或out:[{k},{str(v)}]，请检查')
        if not ans:
            sys.stderr.write(f'注意，没有扫描到测试数据，请检查是否是choose_case的名字写的不准确')

        return ans


if __name__ == '__main__':
    url = 'https://atcoder.jp/contests/jsc2021/tasks/jsc2021_f'
    print(os.path.basename(url))
    print(AtcCaseSpider(url).cases())
    print(AtcCaseSpider(url).cases())
    for i, (case_input, case_output) in enumerate(AtcCaseSpider(url).cases().values(), 1):
        print(f'Case {i} input:')
        print(case_input.strip())
        print(f'Case {i} output:')
        print(case_output)
