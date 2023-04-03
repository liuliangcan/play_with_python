import os
import sys

# from itertools import pairwise
from math import inf

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('../../../../../before20221227/cf/cfinput.txt')
"""https://codeforces.com/problemset/problem/788/A

输入 n(<=1e5) 和长为 n 的整数数组 a(-1e9<=a[i]<=1e9)。
在满足 1<=l<r<=n 的前提下，输出 f(l,r) 的最大值（下列式子中的数组下标从 1 开始）。"""
"""https://codeforces.com/contest/788/submission/118121760

提示 1：奇偶性相同的 l，(-1)^(i-l) 的变化规律是一样的。

提示 2：求的是 abs(a[i]-a[i+1])*(-1)^(i-l) 的最大子段和。

提示 3：对 a 和 a[1:] 分别求一下，取最大值。"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # diff = [abs(a - b) for a, b in pairwise(arr)]
    diff = [abs(arr[i] - arr[i + 1]) for i in range(n - 1)]


    def solve(l):
        ma = dp = -inf
        sign = 1
        for i in range(l, n - 1):
            dp = diff[i] * sign if dp <= 0 else dp + diff[i] * sign
            ma = max(ma, dp)
            sign *= -1
        return ma


    print(max(solve(0), solve(1)))
