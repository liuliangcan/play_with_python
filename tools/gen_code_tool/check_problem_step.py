#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   check_problem_step.py    
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/2/3 15:10    
@Author     :   liushuliang
@Version    :   1.0
@Description:   为了用rust和go补题，自动对比py做过的atc和cf题目，在rust和go对应目录下是否存在文件；
                打印出尚未用rust/go实现的题目
"""
import os

PYTHON_TARGET_DIR = 'F://play_with_code/play_with_python/problem/'
GO_TARGET_DIR = 'F://play_with_code/play_with_go/problem/'
RUST_TARGET_DIR = 'F://play_with_code/play_with_rust/src/problem/'
BEFORE_TARGET_DIR = 'F://play_with_code/play_with_python/before20221227/'

site_tags = ['atc', 'cf']



def check_cha():
    """正则提取茶的url"""
    except_url = {'https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets',
                  ''}
    with open('cha.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    import re

    p = re.compile(r'https://\S+[a-zA-Z0-9_]')  # 匹配https开头 且 字母或数字、下划线结尾的串
    todo = []
    for r in p.findall(text):
        if r not in except_url:
            todo.append(r)
    return todo


todo = check_cha()


def check(site, code_dir):
    """检查对应的目录里的py文件"""
    except_files = {'cf.cpp', 'AtcCaseSpider.py', 'AtcLocalTest.py'}
    s = set()
    for root, dirs, files in os.walk(os.path.join(code_dir, site)):
        for file in files:
            if file in except_files: continue
            pre = file.split('.')[0]
            if pre != 'test':
                s.add(pre)
    return s


def gen_file_name(url):
    """从url产生py文件名"""
    site_tag = ''
    if 'atcoder' in url:
        site_tag = 'atc'
    elif 'codeforces' in url:
        site_tag = 'cf'
    # else:
    #     print('未知的网站链接，无法解析')
    file_name = ''
    if site_tag == 'cf':
        parts = url.split('/')
        contest = f'{site_tag}{parts[-3] if parts[-4] == "contest" else parts[-2]}'  # cf777  由于只给777,rust的mod模块会报命名错误，因此命名为cf777
        task_id = parts[-1].lower()  # d/d2 由于rust大写会报警告，这里统一转小写
        file_name = f"{contest}{task_id}"  # cf777D
    elif site_tag == 'atc':
        parts = url.split('/')
        file_name = parts[-1]  # atc148_c
    return file_name or url



done = []  # 分别统计已整理完成的题目
lower = set()  # 统计已经做了的题目，包括before
for site in site_tags:
    py = check(site, PYTHON_TARGET_DIR)
    go = check(site, GO_TARGET_DIR)
    rust = check(site, RUST_TARGET_DIR)
    if py - go:
        print(f'尚未补齐go代码的题目{site}:{len(py - go)}', py - go)
    if py-rust:
        print(f'尚未补齐rust代码的题目{site}:{len(py - rust)}', py - rust)
    done.append((site, py))

    before = check(site, BEFORE_TARGET_DIR)
    if before-py:
        print(f'尚未整理的以前做的题目{site}:', len(before-py), before-py)
        print()

    for x in py | before:
        lower.add(x.lower())
print('已整理题数:')
cnt = 0
for site, files in done:
    print(f'{site}:{len(files)}')
    cnt += len(files)
print(f'共[{cnt}]题\n')

left = []  # 统计还有多少茶没做
for url in todo:
    name = gen_file_name(url)
    if name not in lower:
        left.append(url)
print('尚未做的茶:', len(left), left)
