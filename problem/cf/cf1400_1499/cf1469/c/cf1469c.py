import collections
import os
import sys
from collections import Counter
from itertools import *

if sys.hexversion == 50924784:
    sys.stdin = open('../../../../../before20221227/cf/cfinput.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1469/C

输入 t(≤1e4) 表示 t 组数据。
每组数据输入 n(2≤n≤2e5) 和 k(2≤k≤1e8) 和长为 n 的数组 h(0≤h[i]≤1e8)。
所有数据的 n 之和不超过 2e5。

你需要在地面上修一个长为 n 的栅栏，地面的海拔高度用 h 数组表示。
你有 n 块高度均为 k 的木板，你需要用这些木板组成栅栏，要求如下：
1. 相邻两块木板的接触长度至少为 1；
2. 第一块和最后一块木板必须正好与地面接触；
3. 其余木板可以与地面接触，或者位于地面之上，每块木板与地面的距离不能超过 k-1。

如果可以修栅栏，输出 YES，否则输出 NO。"""
"""https://codeforces.com/contest/1469/submission/167464872

上下界分析。

维护 l 表示当前木板下边缘的最小海拔，r 表示当前木板下边缘的最大海拔。
对于每个 h[i] 去更新 l 最小能是多少（不能低于 h[i]），更新 r 最大能是多少（不能高于 h[i]+k-1）。
如果更新过程中 l > r 则输出 NO。
如果最后一块木板无法放在地上则输出 NO。
具体实现见代码。"""

def solve1(n, k, hs):
    mn, mx = hs[0], hs[0]  # 当前木板底部位置的上虾界
    for h in hs[1:]:
        mn = max(h, mn - k + 1)
        mx = min(h + k - 1, mx + k - 1)
        if mn > mx:
            return print('NO')

    print('YES' if mn <= hs[-1] <= mx else 'NO')

def solve(n, k, hs):
    mn, mx = hs[0], hs[0]  # 当前木板底部位置的上虾界
    for h in hs[1:]:
        mn = max(h, mn - k + 1)
        mx = min(h + k - 1, mx + k - 1)
        if mn > mx:
            return print('NO')

    print('YES' if mn <= hs[-1] <= mx else 'NO')


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        hs = list(map(int, input().split()))
        solve(n, k, hs)
