import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc237/tasks/abc237_f

输入 n (3≤n≤1000) 和 m (3≤m≤10)。
输出有多少个满足如下条件的数组：
1. 数组长度为 n；
2. 数组元素范围在 [1,m]；
3. 数组的 LIS 的长度恰好等于 3。
对答案模 998244353。

注：LIS 指最长严格上升子序列。
输入 4 5
输出 135

输入 3 4
输出 4

输入 111 3
输出 144980434
https://atcoder.jp/contests/abc237/submissions/35930996

回忆下 LIS 的 O(nlogn) 做法，在那个做法中，我们需要维护一个有序数组 arr。

定义 f[i][x][y][z] 表示长为 i 且 arr=[x,y,z] 的符合题目要求的数组个数。

计算 f[i][x][y][z] 时，枚举第 i 个数是多少，按照 LIS 的 O(nlogn) 做法转移到对应的 x/y/z 上。

代码实现时，可以初始化 f[0][m+1][m+1][m+1] = 1，表示 arr=[inf,inf,inf] 的初始状态。
答案为 sum(f[n][x][y][z])，1≤x<y<z≤m。

为了节省内存，可以将元素值改为从 0 开始。
https://zhuanlan.zhihu.com/p/463478914
"""


#    412	 ms
def solve(n, m):
    # 定义f[i][a][b][c]为前缀a[:i],且长度为123的LIS中结尾最小是是abc的方案数
    f = [[[[0] * (m + 1) for _ in range(m + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    f[0][m][m][m] = 1  # 初始值
    for i in range(1, n + 1):
        for j in range(0, m ):
            for a in range(0, m + 1):
                for b in range(a, m + 1):
                    for c in range(b, m + 1):
                        v = f[i - 1][a][b][c]
                        if j <= a:
                            f[i][j][b][c] += v
                            f[i][j][b][c] %= MOD
                        elif j <= b:
                            f[i][a][j][c] += v
                            f[i][a][j][c] %= MOD
                        elif j <= c:
                            f[i][a][b][j] += v
                            f[i][a][b][j] %= MOD
    ans = 0
    for a in range(0, m):
        for b in range(a + 1, m):
            for c in range(b + 1, m):
                ans = (ans + f[n][a][b][c]) % MOD
    print(ans % MOD)


if __name__ == '__main__':
    n, m = RI()

    solve(n, m)
