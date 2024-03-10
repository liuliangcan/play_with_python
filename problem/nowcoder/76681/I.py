# Problem: 字串比较
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/76681/I
# Memory Limit: 1048576 MB
# Time Limit: 4000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def doubling(s):
    # sa[i]:排名为i的后缀的起始位置
    # rk[i]:起始位置为i的后缀的排名
    n = len(s)
    sa = []
    rk = []
    for i in range(n):
        rk.append(ord(s[i]) - ord('a'))  # 刚开始时，每个后缀的排名按照它们首字母的排序
        sa.append(i)  # 而排名第i的后缀就是从i开始的后缀

    l = 0  # l是已经排好序的长度，现在要按2l长度排序
    sig = 26  # sig是unique的排名的个数，初始是字符集的大小
    while True:
        p = []
        # 对于长度小于l的后缀来说，它们的第二关键字排名肯定是最小的，因为都是空的
        for i in range(n - l, n):
            p.append(i)
        # 对于其它长度的后缀来说，起始位置在`sa[i]`的后缀排名第i，而它的前l个字符恰好是起始位置为`sa[i]-l`的后缀的第二关键字
        for i in range(n):
            if sa[i] >= l:
                p.append(sa[i] - l)
        # 然后开始基数排序，先对第一关键字进行统计
        # 先统计每个值都有多少
        cnt = [0] * sig
        for i in range(n):
            cnt[rk[i]] += 1
        # 做个前缀和，方便基数排序
        for i in range(1, sig):
            cnt[i] += cnt[i - 1]
        # 然后利用基数排序计算新sa
        for i in range(n - 1, -1, -1):
            cnt[rk[p[i]]] -= 1
            sa[cnt[rk[p[i]]]] = p[i]

        # 然后利用新sa计算新rk
        def equal(i, j, l):
            if rk[i] != rk[j]: return False
            if i + l >= n and j + l >= n:
                return True
            if i + l < n and j + l < n:
                return rk[i + l] == rk[j + l]
            return False

        sig = -1
        tmp = [None] * n
        for i in range(n):
            # 直接通过判断第一关键字的排名和第二关键字的排名来确定它们的前2l个字符是否相同
            if i == 0 or not equal(sa[i], sa[i - 1], l):
                sig += 1
            tmp[sa[i]] = sig
        rk = tmp
        sig += 1
        if sig == n:
            break
        # 更新有效长度
        l = l << 1 if l > 0 else 1
    # 计算height数组
    k = 0
    height = [0] * n
    for i in range(n):
        if rk[i] > 0:
            j = sa[rk[i] - 1]
            while i + k < n and j + k < n and s[i + k] == s[j + k]:
                k += 1
            height[rk[i]] = k
            k = max(0, k - 1)  # 下一个height的值至少从max(0,k-1)开始
    return sa, rk, height


RANDOM = random.randint(37, 100)  # 这里一定搞个全局的，切记切记：如果题目里需要对多个字符串分别哈希，同样的base和mod才能比较


class StringHash:
    """字符串哈希，用O(n)时间预处理，用O(1)时间获取段的哈希值"""

    def __init__(self, s):
        n = len(s)
        self.BASE = BASE = 131 + RANDOM  # 进制 131,131313
        self.MOD = MOD = 10 ** 13 + RANDOM  # 10**9+7,998244353,10**13+7
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * BASE) % MOD
            h[i] = (h[i - 1] * BASE % MOD + ord(s[i - 1])) % MOD

    def get_hash(self, l, r):
        """用O(1)时间获取开区间[l,r)（即s[l:r]）的哈希值"""
        return (self.h[r] - self.h[l] * self.p[r - l] % self.MOD) % self.MOD


# print(doubling('abcd'))
#       ms
def solve():
    n, m, q = RI()
    s1, = RS()
    s2, = RS()
    sh1 = StringHash(s1)
    sh2 = StringHash(s2)
    rk = doubling(s1 + s2)[1]
    for _ in range(q):
        l1, r1, l2, r2 = RI()
        if sh1.get_hash(l1 - 1, r1) == sh2.get_hash(l2 - 1, r2):
            print('=')
        else:
            x, y = rk[l1 - 1], rk[n + l2 - 1]
            if x < y:
                print('<')
            else:
                print('>')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
