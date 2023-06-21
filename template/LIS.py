"""LIS\LCS"""
import collections
import itertools
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def lis(nums):
            n = len(nums)
            # dp = [float('inf')] * (n+1)  # dp[i](从1开始) 为长度为i的上升子序列的可以的最小尾巴
            dp = []
            for num in nums:
                if not dp or num > dp[-1]:
                    dp.append(num)
                else:
                    pos = bisect_left(dp,num)
                    dp[pos] = num
            return len(dp)

        return lis(nums)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lis_nlgn(nums):
            n = len(nums)
            # dp = [float('inf')] * (n+1)  # dp[i] 为长度为i的上升子序列的可以的最小尾巴
            dp = []
            for num in nums:
                if not dp or num > dp[-1]:
                    dp.append(num)
                else:
                    pos = bisect_left(dp, num)
                    dp[pos] = num
            return len(dp)

        def lcs_nlgn(s1, s2):
            s1_poses = collections.defaultdict(list)
            for i in range(len(s1) - 1, -1, -1):  # 需要逆序
                s1_poses[s1[i]].append(i)
            cleaned_s2_pos = list(itertools.chain.from_iterable([s1_poses[x] for x in s2 if x in s1_poses]))
            same_lis = lis_nlgn(cleaned_s2_pos)
            return same_lis

        def lcs_n2(s1, s2):
            m, n = len(s1), len(s2)
            dp = [[0] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if s1[i - 1] == s2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            return dp[m][n]

        return lcs_nlgn(text1, text2)
