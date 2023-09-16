# Problem: 小苯的带猫猫任务
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65319/G
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

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

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """不会是同余方程吧，不会
考虑处理第i只猫的情况： pos like w left right
1. 收益是固定的，那么只需要考虑最低体力消耗是多少，然后背包
2. 假设向左x次，向右y次，须满足：pos - left*x + right*y = 0 mod like  (枚举x求y？)    
3. 消耗体力cost = p*x + q*y,求最小cost

# 由于1<=pq,k<=1e3好像可以枚举左右次数，用同余哈希表硬搞？
"""


#       ms
def solve():
    n, p, q, k = RI()
    f = [0] + [0] * k  # 背包最多用k消耗获取最大价值
    ans = 0  # 无需移动就能得的
    for _ in range(n):
        pos, like, w, left, right = RI()
        if pos % like == 0:
            ans += w
            continue
        vis = {pos % like: 0}
        mn = k + 1  # 最低消耗，不会超过k
        for i in range(1, k // p + 1):  # 枚举向左跳的次数，最多把体力用完，不会超过1e3次
            pos1 = (pos - left * i) % like  # 向左能跳到的位置
            if pos1 in vis: break  # 跳到重复点就会进入循环
            vis[pos1] = p * i  # 到这个点的消耗
            if pos1 == 0:  # 只向左就可以
                mn = p * i

        for i in range(1, k // q + 1):  # 枚举向右的步数
            r = right * i  # (r+pos1)%like = 0
            mn = min(mn, vis.get((like - r) % like, k + 1) + i * q)  # 这个组合在

        if mn <= k:
            for j in range(k, mn - 1, -1):
                f[j] = max(f[j], f[j - mn] + w)

    print(ans + f[-1])


#       ms
def solve1():
    n, p, q, k = RI()
    f = [0] + [0] * k  # 背包最多用k消耗获取最大价值
    ans = 0
    for _ in range(n):
        pos, like, w, left, right = RI()
        if pos % like == 0:
            ans += w
            continue
        vis = {pos % like: 0}
        mn = k + 1
        for i in range(1, k // p + 1):  # 枚举向左跳的次数，最多把体力用完，不会超过1e3次
            pos1 = (pos - left * i) % like
            if pos1 in vis: break  # 跳到重复点就会进入循环
            vis[pos1] = p * i
            if pos1 == 0:  # 只向左可以
                mn = min(mn, p * i)

        for i in range(1, k // q + 1):
            r = right * i  # (r+pos1)%like = 0
            l = (like - r) % like
            if l in vis:
                mn = min(mn, vis[l] + i * q)
        if mn <= k:
            for j in range(k, mn - 1, -1):
                f[j] = max(f[j], f[j - mn] + w)

    print(ans + f[-1])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
