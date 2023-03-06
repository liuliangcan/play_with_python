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

site_tags = ['atc', 'cf']


def check(site, code_dir):
    s = set()
    for root, dirs, files in os.walk(os.path.join(code_dir, site)):
        for file in files:
            pre = file.split('.')[0]
            if pre != 'test':
                s.add(pre)
    return s


cnt = []
for site in site_tags:
    py = check(site, PYTHON_TARGET_DIR)
    go = check(site, GO_TARGET_DIR)
    rust = check(site, RUST_TARGET_DIR)
    print(len(py - go), py - go)
    print(len(py - rust), py - rust)
    cnt.append((site, len(py)))
print('刷题数:', cnt, f'共:{sum(x for _, x in cnt)}')
