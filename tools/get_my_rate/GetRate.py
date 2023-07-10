#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   GetRate.py    
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/7/10 11:17    
@Author     :   liushuliang
@Version    :   1.0
@Description:   None
"""
import requests
from lxml import etree



class GetRate:
    def __init__(self):
        self.base_url = ''
        self.target_user = ''
        self.url = ''
        self.xpath = ''


    def get_content(self):
        payload = {}
        headers = {}
        response = requests.request("GET", self.url, headers=headers, data=payload)
        # print(response.text)
        return response.text
    def make_url(self):
        self.url = self.base_url.format(user=self.target_user)

    def get_rate(self):
        self.make_url()
        content = self.get_content()

        html = etree.HTML(content)
        sections = html.xpath(self.xpath)

        # print(sections)
        return sections[0]

class GetRateFactory:
    def __init__(self):
        pass
    @staticmethod
    def get(tag,user):
        # print(tag)
        assert tag
        from tools.get_my_rate.GetRateAcwing import GetRateAcwing
        from tools.get_my_rate.GetRateAtcoder import GetRateAtcoder
        from tools.get_my_rate.GetRateCodeChef import GetRateCodeChef
        from tools.get_my_rate.GetRateCodeforces import GetRateCodeforces
        from tools.get_my_rate.GetRateLeetcodeCN import GetRateLeetcodeCN
        from tools.get_my_rate.GetRateNowcoder import GetRateNowcoder
        if 'awc' in tag or tag.lower() == 'acwing':
            return GetRateAcwing(user)
        if 'lccn' in tag or tag.lower() == 'leetcodecn':
            return GetRateLeetcodeCN(user)
        if 'nc' in tag or tag.lower() == 'nowcoder':
            return GetRateNowcoder(user)
        if 'atc' in tag or tag.lower() == 'atcoder':
            return GetRateAtcoder(user)
        if 'cf' in tag or tag.lower() == 'codeforces':
            return GetRateCodeforces(user)
        if 'cc' in tag or tag.lower() == 'codechef':
            return GetRateCodeChef(user)
        return None
