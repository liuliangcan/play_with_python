#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   get_rate.py    
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/7/10 12:51    
@Author     :   liushuliang
@Version    :   1.0
@Description:   拉取常用竞赛网站的竞赛分
"""
from tools.get_my_rate.GetRate import GetRateFactory

me = [
    ('acwing', '204427'),
    ('leetcodecn', 'liuliangcan'),
    ('nowcoder', '9489028'),
    ('atcoder', 'qishui'),
    ('codeforces', 'qishui7'),
    ('codechef', 'qishui7'),
]

for tag, user in me:
    rate = GetRateFactory.get(tag, user).get_rate()
    print(user, tag, rate)
