import collections
import io
import os
import sys
from bisect import bisect_right
from collections import deque

if os.getenv('LOCALTESTLUOGU'):
    sys.stdin = open('input.txt')


# def solve(n, a):
#     dp = [[0] * 2 for _ in range(n)]
#     print(n,a)
#     dp[0][1] = a[0][0]
#     for i in range(1, n):
#         w, s = a[i]
#         dp[i][0] = max(dp[i - 1])
#         for j in range(i - 1, -1, -1):
#             if j + a[j][1] < i:
#                 # print(j,s,i)
#                 dp[i][1] = max(dp[j][1] + w, dp[i][1])
#         # print(dp)
#
#     print(max(dp[-1]))

def solve(n, a):
    ends = collections.defaultdict(list)  # 计算以每个西瓜为起始，前边可以正好最后取谁
    for i, (_, s) in enumerate(a):
        ends[i + s+1].append(i)
    dp = [0] * n  # 在第i个西瓜的最大值
    dp[0] = a[0][0]
    for i in range(1, n):
        w, s = a[i]
        dp[i] = dp[i - 1]  # 第i个西瓜不取
        for j in ends[i]:
            dp[i] = max(dp[i], dp[j] + w)  # 尝试用第j个西瓜转移
        # print(dp)

    print(dp[-1])


if __name__ == '__main__':
    nums =   [2,10,2019]
    l = -1
    r = 0
    n = len(nums)
    ans = 0
    for i,a in enumerate(nums):
        if a == 0:
            if l == -1:
                l = r = i
            else:
                r = i
        else:
            if l != -1:
                # print(l,r)
                # ans += 2**(r - l + 1)-1
                ans += (r - l + 1)*(r-l+2)//2
                l = -1
    if l!=-1:
        ans += (r - l + 1)*(r-l+2)//2
    print(ans)

