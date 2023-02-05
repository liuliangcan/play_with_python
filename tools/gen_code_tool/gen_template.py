#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   gen_template.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/2/2 19:14    
@Author     :   liushuliang
@Version    :   1.0
@Description:   根据url，生成go和rust的 刷题/测试 代码文件；但手动提交
"""
from tools.gen_code_tool.AtcGenTemplate import AtcGenTemplate

url = 'https://atcoder.jp/contests/abc272/tasks/abc272_e'
AtcGenTemplate(url).run()
