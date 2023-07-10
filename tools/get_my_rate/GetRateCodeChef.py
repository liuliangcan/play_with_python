#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   GetRateCodeChef.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/7/10 12:46
@Author     :   liushuliang
@Version    :   1.0
@Description:   None
"""

from lxml import etree
from tools.get_my_rate.GetRate import GetRate

class GetRateCodeChef(GetRate):
    def __init__(self, target_user=None):
        super().__init__()
        self.base_url = 'https://www.codechef.com/users/{user}'
        self.target_user = target_user
        self.xpath = '/html/body/main/div/div/div/aside/div/div/div/div/text()'
        # '/html/body/main/div/div/div/aside/div[1]/div/div[1]/div[1]'

    def get_rate(self):
        self.make_url()
        content = self.get_content()

        html = etree.HTML(content)
        sections = html.xpath(self.xpath)

        # print(sections)
        return sections[0]


if __name__ == '__main__':
    cc = GetRateCodeChef('qishui7').get_rate()  # 1366
    print(cc)
