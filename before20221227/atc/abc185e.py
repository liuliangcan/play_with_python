import sys
from collections import *
from itertools import *
from math import sqrt, inf
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

MOD = 10 ** 9 + 7
"""https://atcoder.jp/contests/abc185/tasks/abc185_e

输入 n(≤1000) 和 m(≤1000)，长度分别为 n 和 m 的数组 a 和 b，元素范围 [1,1e9]。
从 a 中移除若干元素，得到一个子序列 a'；从 b 中移除若干元素，得到一个子序列 b'。
要求 a' 和 b' 的长度相同。
输出 (a和b总共移除的元素个数) + (a'[i]≠b'[i]的i的个数) 的最小值。
输入
4 3
1 2 1 3
1 3 1
输出 2

输入
4 6
1 3 2 4
1 5 2 6 4 3
输出 3

输入
5 5
1 1 1 1 1
2 2 2 2 2
输出 5
https://atcoder.jp/contests/abc185/submissions/36352936

类似 LCS，定义 f[i][j] 表示 a 的前 i 个元素和 b 的前 j 的元素算出的答案。

- 不选 a[i] 选 a[j]：f[i-1][j]+1
- 选 a[i] 不选 a[j]：f[i][j-1]+1
- 选 a[i] 选 a[j]：f[i-1][j-1] + (a[i]==a[j] ? 0 : 1)
取最小值。

注：都不选是不用考虑的，这已经包含在 f[i-1][j] 或者 f[i][j-1] 中了。
也可以这么想：都不选是不如都选的。

边界：f[0][i]=f[i][0]=i。
答案：f[n][m]。
"""


#   670  	 ms
def solve(n, m, a, b):
    # f[i][j]表示a前i个数、b前[j]个数的答案
    # 如果a[i]==b[j],显然可以无伤增加f[i][j] = f[i-1][j-1]
    # 否则只需修改其中一个使他们相等f[i][j] = f[i-1][j-1]+1
    # 另外,参考LCS,计算从分别少一个的情况转移而来，只需补齐一个相同字符。
    # 实现时，f整体向右便宜，以便处理初始状态
    f = [[inf] * (m + 1) for _ in range(n + 1)]
    for i in range(n+1):
        f[i][0] = i
    for j in range(m+1):
        f[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            f[i][j] = min(f[i][j], f[i - 1][j] + 1, f[i][j - 1] + 1, f[i - 1][j - 1] + 1)

    print(f[-1][-1])


if __name__ == '__main__':
    n, m = RI()
    a = RILST()
    b = RILST()

    solve(n, m, a, b)
