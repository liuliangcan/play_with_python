import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: sys.stdin.readline().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/837/D

输入 n k (1≤k≤n≤200) 和一个长为 n 的数组 a (1≤a[i]≤1e18)。
从 a 中选择一个长为 k 的子序列，设这 k 个数的乘积为 m。
输出 m 的末尾 0 的个数的最大值。

子序列不一定连续。
输入
3 2
50 4 20
输出 3
解释 选择 [50,20]，m=1000

输入
5 3
15 16 3 25 9
输出 3
解释 选择 [15,16,25]，m=6000

输入
3 3
9 77 13
输出 0
解释 选择 [9,77,13]，m=9009  

https://codeforces.com/contest/837/submission/172210710
循环优化 https://codeforces.com/contest/837/submission/172219030

提示 1：转换成二维费用的 01 背包。

提示 2：物品可以看成「个数=1个，体积=因子5的个数，价值=因子2的个数」。

提示 3：定义 f[i][j][p] 表示前 i 个数字，选 j 个，因子 5 的个数等于 p 时，因子 2 的个数的最大值。

根据 01 背包，有 f[i][j][p] = max(f[i-1][j][p], f[i-1][j-1][p-cnt5[i]] + cnt2[i])。其中 cnt2[i] 和 cnt5[i] 为 a[i] 的因子 2 和因子 5 的个数。
初始项 f[0][0][0] = 0，其余为 -∞。
答案为 max{min(i, f[n][k][i])}。
代码实现时，第一个维度可以优化掉。(倒序循环）

注：对于每个数，因子 5 的个数至多有 25 个。
"""


def get_2_5_cnt(x):
    t, f = 0, 0
    while x % 2 == 0:
        t += 1
        x //= 2
    while x % 5 == 0:
        f += 1
        x //= 5
    return t, f


# 	 ms
def solve(n, k, a):
    dp = [[-inf] * (k * 25 + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for v in a:
        t, f = get_2_5_cnt(v)
        for i in range(k, 0, -1):
            for j in range(k * 25, f - 1, -1):
                if dp[i - 1][j - f] >= 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - f] + t)
    # print(dp)
    ans = 0
    for i, v in enumerate(dp[k]):
        ans = max(ans, min(i, v))
    print(ans)


if __name__ == '__main__':
    n, k = RI()
    a = RILST()

    solve(n, k, a)
