import os
import sys

if os.getenv('TESTLIU'):
    sys.stdin = open('input.txt')

N, V = map(int, input().split())
goods = []
for i in range(N):
    goods.append(tuple(map(int, input().split())))
# print(goods)
dp = [0] * (V + 1)
# dp[i][j] 表示选前i件物品，总体积j时最大价值
# 放i时，选或不选i，dp[i][j] = max(dp[i-1][j-v[i]]+w[i],dp[i-1][j])
for i in range(N):
    v, w, s = goods[i]
    for k in range(s):
        for j in range(V, v - 1, -1):
            dp[j] = max(dp[j - v] + w, dp[j])
    # print(dp)

# print(dp)
print(dp[V])
