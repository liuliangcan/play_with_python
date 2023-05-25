# Problem: F. Ira and Flamenco
# Contest: Codeforces - Codeforces Round 874 (Div. 3)
# URL: https://codeforces.com/contest/1833/problem/F
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from collections import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，实测这个快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """输入n,m和长为n的数组a[i]。
你需要从中选m个数。其中每两个数都不同，且每两个数的差值严格小于m。
问有多少种方案。下标不同则视为不同方案。
"""
"""逆元/区间乘/乘法原理
看错题很久， 后来发现严格选m个数，且差值小于m，那只能选一段连续的数字。
每个数字有cnt[x]个，那么乘法原理计算即可。剩下的问题就是区间乘怎么弄。
可以滑窗，维护长为m的段，合法情况是段首段尾的值正好差m-1。
每次乘上窗右侧，除去窗左侧出窗的数即可，由于除法不满足同余，因此要乘逆元logn。
但直接预处理前缀乘，就可以O(n)计算每个逆元。
---
赛后卡哈希了，哭了。
---
针对Counter卡哈希的话，事先给arr排序就可以了。
"""


#     tle  ms
def solve4():
    n, m = RI()
    a = RILST()
    cnt = Counter(a)
    b = sorted(cnt.keys())
    fact = [1]
    for v in b:
        fact.append(fact[-1] * cnt[v] % MOD)
    inv = [1] * len(fact)
    inv[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(len(b) - 1, -1, -1):
        inv[i] = cnt[b[i]] * inv[i + 1] % MOD

    ans = 0
    for i in range(m - 1, len(b)):
        j = i - m + 1
        if j >= 0 and b[j] == b[i] - m + 1:
            ans = (ans + fact[i + 1] * inv[j]) % MOD

    print(ans % MOD)


#       ms
def solve():
    n, m = RI()
    a = RILST()
    cnt = Counter(a)
    b = sorted((k, v) for k, v in cnt.items())
    fact = [1]
    for c,v in b:
        fact.append(fact[-1] * v % MOD)
    inv = [1] * len(fact)
    inv[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(len(b) - 1, -1, -1):
        inv[i] = b[i][1] * inv[i + 1] % MOD

    ans = 0
    for i in range(m - 1, len(b)):
        j = i - m + 1
        if j >= 0 and b[j][0] == b[i][0] - m + 1:
            ans = (ans + fact[i + 1] * inv[j]) % MOD

    print(ans % MOD)


#     202  ms
def solve1():
    n, m = RI()
    a = RILST()
    a.sort()
    b, cnt = [], []
    for i, v in enumerate(a):
        if i == 0 or v != a[i - 1]:
            b += [v]
            cnt += [1]
        else:
            cnt[-1] += 1
    fact = [1]
    for v in cnt:
        fact.append(fact[-1] * v % MOD)
    inv = [1] * len(fact)
    inv[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(len(b) - 1, -1, -1):
        inv[i] = cnt[i] * inv[i + 1] % MOD

    ans = 0
    for i in range(m - 1, len(b)):
        j = i - m + 1
        if j >= 0 and b[j] == b[i] - m + 1:
            ans = (ans + fact[i + 1] * inv[j]) % MOD

    print(ans % MOD)


#     592  ms
def solve2():
    n, m = RI()
    a = RILST()
    cnt = Counter(a)
    b = sorted(cnt.keys())
    cur = 1
    ans = 0
    for i, v in enumerate(b):
        cur = cur * cnt[v] % MOD
        j = i - m + 1
        if j > 0:
            cur = cur * pow(cnt[b[j - 1]], MOD - 2, MOD) % MOD
        if j >= 0 and b[j] == b[i] - m + 1:
            ans = (ans + cur) % MOD

    print(ans % MOD)


class ModPreMul:
    """带模区间乘，O(n)预处理逆元和前缀乘，O(1)查询"""

    def __init__(self, a, p=10 ** 9 + 7):
        n = len(a)
        self.p = p
        self.fact = fact = [1] * (n + 1)
        self.inv = inv = [1] * (n + 1)
        for i, v in enumerate(a, start=1):
            fact[i] = fact[i - 1] * v % p
        inv[-1] = pow(fact[-1], p - 2, p)
        for i in range(n - 1, -1, -1):
            inv[i] = a[i] * inv[i + 1] % p

    def mul_interval(self, l, r):
        return self.fact[r + 1] * self.inv[l] % self.p


#     59  ms
def solve4():
    n, m = RI()
    a = RILST()
    cnt = Counter(a)
    b = sorted(cnt.keys())
    c = [cnt[v] for v in b]
    mp = ModPreMul(c, MOD)
    ans = 0
    for i, v in enumerate(b):
        j = i - m + 1
        if j >= 0 and b[j] == b[i] - m + 1:
            ans = (ans + mp.mul_interval(j, i)) % MOD

    print(ans % MOD)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
