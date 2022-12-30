from collections import *
import math
import random
import urllib.parse
from collections import *
from functools import cache, reduce
from graphlib import TopologicalSorter
from operator import add, sub
from typing import *

# Definition for a binary tree node.
from sortedcontainers import SortedList
import re

MOD = 10 ** 9 + 7

primes = [1] * 10001
primes[0] = 0
primes[1] = 1
for i in range(2, 10000):
    if primes[i]:
        for j in range(2 * i, 10001, i):
            primes[j] = 0

ABC = {2, 3, 5, 7}


@cache
def get_prime_reasons(x):  # 计算x的分解质因数结果：每个质因数和它出现的次数。
    if x == 1:
        return Counter()
    if primes[x]:
        return Counter([x])
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return get_prime_reasons(i) + get_prime_reasons(x // i)


ps = {2, 3, 5}


@cache
def ugly(x):
    if x == 1:
        return True
    c = get_prime_reasons(x)

    return len(set(c.keys()) - ps) == 0


class StringHash:
    # 字符串哈希，用O(n)时间预处理，用O(1)时间获取段的哈希值
    def __init__(self, s):
        n = len(s)
        self.BASE = BASE = 131  # 进制 131,131313
        self.MOD = MOD = 10 ** 9 + 7  # 10**9+7，998244353
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * BASE) % MOD
            h[i] = (h[i - 1] * BASE % MOD + ord(s[i - 1])) % MOD

    # 用O(1)时间获取开区间[l,r)（即s[l:r]）的哈希值，比切片要快
    def get_hash(self, l, r):
        return (self.h[r] - self.h[l] * self.p[r - l] % self.MOD) % self.MOD

    # 用O(1)时间获取开区间[l,r)（即s[l:r]）的哈希值；这个实测会TLE，不如用self.get_hash
    def __getitem__(self, index):
        if isinstance(index, slice):
            l, r, step = index.indices(len(self.h)-1)
            if step != 1:
                raise Exception('StringHash slice 步数仅限1'+str(index))
            return (self.h[r] - self.h[l] * self.p[r - l] % self.MOD) % self.MOD
        else:
            return (self.h[index+1] - self.h[index] * self.p[index+1 - index] % self.MOD) % self.MOD

class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        sh = StringHash(s)
        f = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, (i + n) // 2 + 1):
                if sh[i:j] == sh[j: j + j - i]:
                    f[i] = max(f[i], f[j] + 1)
        return f[0]

if __name__ == '__main__':
    string1 = ['leetcode', 'leet', 'happycode', 'lee']
    string2 = ['l', 'la', 'lb', 'lx', 'lxa', 'lxb']
    string3 = ['l', 'la', 'lb', 'lc', 'ld', 'le']
    s = "abcabcdabc"
    print(Solution().deleteString(s))
