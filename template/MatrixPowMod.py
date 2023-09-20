"""
矩阵快速幂，要求矩阵是正方形，可以把线性dp的O(n)优化成O(lgn)
https://leetcode.cn/problems/string-transformation/
"""
MOD = 10 ** 9 + 7


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


def matrix_multiply(a, b, MOD=10 ** 9 + 7):
    m, n, p = len(a), len(a[0]), len(b[0])
    ans = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                ans[i][k] = (ans[i][k] + a[i][j] * b[j][k]) % MOD
    return ans


def matrix_pow_mod(a, b, MOD=10 ** 9 + 7):
    n = len(a)
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1
    while b:
        if b & 1:
            ans = matrix_multiply(ans, a, MOD)
        a = matrix_multiply(a, a, MOD)
        b >>= 1
    return ans


class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        if t not in s + s:
            return 0
        n = len(s)
        c = len(list(Kmp(t).find_all_yield(s + s[:-1])))
        m = [
            [c - 1, c],
            [n - c, n - 1 - c]
        ]
        m = matrix_pow_mod(m, k)
        return m[0][s != t]


MOD = 10 ** 9 + 7

import numpy as np


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """https://leetcode.cn/problems/count-vowels-permutation/description/
        定义f[i][0~4]表示长为i+1的字符串，最后结尾是aeiou的种类数
        显然f[0][0:5] = [1,1,1,1,1]
        下边g = f[i-1]
        f[i][0] = 0g[0] + 1g[1] + 1g[2] + 0g[3] + 1g[4]
        f[i][1] = 1g[0] + 0g[1] + 1g[2] + 0g[3] + 0g[4]
        f[i][2] = 0g[0] + 1g[1] + 0g[2] + 1g[3] + 0g[4]
        f[i][3] = 0g[0] + 0g[1] + 1g[2] + 0g[3] + 0g[4]
        f[i][4] = 0g[0] + 0g[1] + 1g[2] + 1g[3] + 0g[4]
        """
        if n == 1:
            return 5
        m = np.mat([
            [0, 1, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 1, 0]
        ])
        f0 = np.mat([
            [1],
            [1],
            [1],
            [1],
            [1],
        ])
        n -= 1
        while n:
            if n & 1:
                f0 = m * f0 % MOD
            m = m * m % MOD
            n >>= 1
        return int(f0.sum()) % MOD
