"""Z函数，国内也喜欢叫扩展KMP。
z[i]表示s[i:]和s[0:]的最长公共前缀长度.
用途：
1. 当KMP用:从s里搜t的所有出现，只需构造一个t#s,那么s对应的z[i]==|t|的，就是出现位置。
2. 字符串整周期：给定一个长度为 n 的字符串 s，找到其最短的整周期，即寻找一个最短的字符串 t，使得 s 可以被若干个 t 拼接而成的字符串表示。
    计算s的Z函数，整周期则是最小的i满足i+z[i]==n。
简介(和manacher很像)：
1. 维护一个当前最右的匹配区间[L,R]，称作z-box。我们知道s[L~R]==s[0~R-L]
2. 那么如果i落在[L,R]里，z[i]则可以等于z[i-L]。不需要从0开始枚举，是实现了加速。
复杂度：初始化O(n)
1. 证明也类似马拉车，每个位置只会被扩展（内层循环）成功一次。
特殊: 规定z[0]=0。
例题:
1. Z函数匹配前后缀。https://leetcode.cn/problems/minimum-time-to-revert-word-to-initial-state-ii/description/
2. 前后中缀匹配：Z函数+前后缀分解 https://codeforces.com/problemset/problem/126/B
3.
"""


class ZFunction:
    # def __init__(self, s):

    def __init__(self, s):
        n = len(s)
        self.z = z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r and z[i - l] < r - i + 1:
                z[i] = z[i - l]
            else:
                z[i] = max(0, r - i + 1)
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
    @staticmethod
    def find_all_match_pos(s, t):
        """从s中找到所有t的位置"""
        s = t + '#' + s
        n = len(t)
        z = ZFunction(s).z
        ans = []
        for i in range(n + 1, len(s)):
            if z[i] == n:
                ans.append(i - n - 1)
        return ans
# class Solution:
#     def minimumTimeToInitialState(self, word: str, k: int) -> int:
#         z = ZFunction(word).z
#         n = len(word)
#         for i in range(k,n,k):
#             if z[i] == n-i:
#                 return i//k
#         return (n+k-1)//k
#
# s = 'aeebcbefef'
# t = 'ef'
# print(ZFunction.find_all_match_pos(s,t))
#     n = len(s)
#     self.z = z = [0] * n
#     l = r = 0
#     for i in range(1, n):
#         if i <= r:
#             z[i] = min(z[i - l], r - i + 1)
#         while i + z[i] < n and s[z[i]] == s[i + z[i]]:  # 更简单的写法，但是慢一点
#             l, r = i, i + z[i]
#             z[i] += 1