
class Kmp:
    """kmp算法，计算前缀函数pi,根据pi转移，复杂度O(m+n)"""

    def __init__(self, t):
        """传入模式串，计算前缀函数"""
        self.t = t
        n = len(t)
        self.pi = pi = [0] * n
        j = 0
        for i in range(1, n):
            while j and t[i] != t[j]:
                j = pi[j - 1]  # 失配后缩短期望匹配长度
            if t[i] == t[j]:
                j += 1  # 多配一个
            pi[i] = j

    def find_all_yield(self, s):
        """查找t在s中的所有位置，注意可能为空"""
        n, t, pi, j = len(self.t), self.t, self.pi, 0
        for i, v in enumerate(s):
            while j and v != t[j]:
                j = pi[j - 1]
            if v == t[j]:
                j += 1
            if j == n:
                yield i - j + 1
                j = pi[j - 1]

    def find_one(self, s):
        """查找t在s中的第一个位置，如果不存在就返回-1"""
        for ans in self.find_all_yield(s):
            return ans
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        kmp = Kmp(needle)
        return kmp.find_one(haystack)
