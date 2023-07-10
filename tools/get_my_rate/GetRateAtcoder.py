#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   GetRateAtcoder.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/7/10 11:44
@Author     :   liushuliang
@Version    :   1.0
@Description:   None
"""

import requests
from lxml import etree
from tools.get_my_rate.GetRate import GetRate


class GetRateAtcoder(GetRate):
    def __init__(self, target_user=None):
        super().__init__()
        self.base_url = 'https://atcoder.jp/users/{user}'
        self.target_user = target_user
        self.xpath = '/html/body/div/div/div/div/table/tr/td/span/text()'
        # '/html/body/div[1]/div/div[1]/div[3]/table/tbody/tr[2]/td/span'


if __name__ == '__main__':
    atc = GetRateAtcoder('tourist').get_rate()  # 3889
    print(atc)  #
