#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   make_data.py    
@License    :   (C)Copyright 2013-2022, capstone
@Project    :   NormalTools
@Software   :   PyCharm
@ModifyTime :   2022/8/18 14:22    
@Author     :   liushuliang
@Version    :   1.0
@Description:   None
"""

import  random

up = 2*10**5
n = 10000
with open('data.txt','w') as f:

    f.write(f'{10000}\n')
    for _ in range(1000):
        f.write(f'{n} ')
        n-=1
