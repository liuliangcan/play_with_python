#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   GetRateNowcoder.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/7/10 12:42
@Author     :   liushuliang
@Version    :   1.0
@Description:   None
"""

from lxml import etree
from tools.get_my_rate.GetRate import GetRate

class GetRateNowcoder(GetRate):
    def __init__(self, target_user=None):
        super().__init__()
        self.base_url = 'https://ac.nowcoder.com/acm/contest/profile/{user}'
        self.target_user = target_user
        self.xpath = '/html/body/div/div/div/section/div/div/div/text()'
        # '/html/body/div[1]/div[2]/div[2]/section/div[1]/div[1]/div'



if __name__ == '__main__':
    nc = GetRateNowcoder('9489028').get_rate()  # 1366
    print(nc)
