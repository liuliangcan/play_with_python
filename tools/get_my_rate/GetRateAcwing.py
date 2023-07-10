#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   GetRateAcwing.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/7/10 11:36
@Author     :   liushuliang
@Version    :   1.0
@Description:   None
"""

from lxml import etree
from tools.get_my_rate.GetRate import GetRate

class GetRateAcwing(GetRate):
    def __init__(self, target_user=None):
        super().__init__()
        self.base_url = 'https://www.acwing.com/user/myspace/activity/{user}/1/competition/'
        self.target_user = target_user
        self.xpath = '/html/body/div/div/div/div/div/div/div/h4/strong/text()'



if __name__ == '__main__':
    acw = GetRateAcwing('204427').get_rate()
    print(acw)
