#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   GetRateCodeforces.py    
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/7/10 11:20    
@Author     :   liushuliang
@Version    :   1.0
@Description:   None
"""

from lxml import etree
from tools.get_my_rate.GetRate import GetRate


class GetRateCodeforces(GetRate):
    def __init__(self, target_user=None):
        super().__init__()
        self.base_url = 'https://codeforces.com/profile/{user}'
        self.target_user = target_user
        self.xpath = '/html/body/div/div/div/div/div/div/ul/li/span[@style="font-weight:bold;"]/text()'


if __name__ == '__main__':
    cf = GetRateCodeforces('qishui7').get_rate()
    print(cf)
