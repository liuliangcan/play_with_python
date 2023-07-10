#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File       :   GetRateLeetcodeCN.py
@License    :   (C)Copyright 2013-2023, capstone
@Project    :   play_with_python
@Software   :   PyCharm
@ModifyTime :   2023/7/10 12:34
@Author     :   liushuliang
@Version    :   1.0
@Description:   None
"""
import json

import requests
from lxml import etree
from tools.get_my_rate.GetRate import GetRate

class GetRateLeetcodeCN(GetRate):
    def __init__(self, target_user=None):
        super().__init__()
        self.base_url = 'https://leetcode.cn/graphql/noj-go/'
        self.target_user = target_user
        self.xpath = '/html/body/div/div/div/div/table/tr/td/span/text()'
        # '/html/body/div[1]/div/div[1]/div[3]/table/tbody/tr[2]/td/span'


    def get_rate(self):
        return self.get_user_score_info(self.target_user)

    def get_user_score_info(self, user):
        """获取用户当前的分数信息"""
        data = {
            "query": "query userContestRankingInfo($userSlug: String!) {\n  userContestRanking(userSlug: $userSlug) {\n    attendedContestsCount\n    rating\n    globalRanking\n    localRanking\n    globalTotalParticipants\n    localTotalParticipants\n    topPercentage\n  }\n  userContestRankingHistory(userSlug: $userSlug) {\n    attended\n    totalProblems\n    trendingDirection\n    finishTimeInSeconds\n    rating\n    score\n    ranking\n    contest {\n      title\n      titleCn\n      startTime\n    }\n  }\n}\n    ",
            "variables": {
                "userSlug": user
            }
        }
        headers = {
            "content-type": "application/json",
        }
        # print(self.base_url)
        res = requests.post(self.base_url, data=json.dumps(
            data), headers=headers)
        data = res.json().get('data')
        if not data:
            return 0
        data = data.get('userContestRanking')
        if not data:
            return 0
        score = data.get('rating')
        if not score:
            return 0
        return score

if __name__ == '__main__':
    lccn = GetRateLeetcodeCN('liuliangcan').get_rate()  # 2525
    print(lccn)  #
