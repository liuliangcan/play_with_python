import io
import os
import sys
from collections import deque

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

# 注意这里多重背包是二进制优化，过不了
def solve(N, V, goods):
    dp = [0] * (V + 1)

    def zero_one_pack(v, w):
        for j in range(V, v - 1, -1):
            dp[j] = max(dp[j - v] + w, dp[j])

    def complete_pack(v, w):
        for j in range(v, V + 1):
            dp[j] = max(dp[j - v] + w, dp[j])

    def multi_pack_binary(v, w, s):
        if v * s >= V:
            return complete_pack(v, w)
        k = 1
        while k < s:
            for j in range(V, v * k - 1, -1):
                dp[j] = max(dp[j - v * k] + w * k, dp[j])
            s -= k
            k <<= 1

        for j in range(V, v * s - 1, -1):
            dp[j] = max(dp[j - v * s] + w * s, dp[j])

    for v, w, s in goods:
        multi_pack_binary(v, w, s)

    print(dp[V])


if __name__ == '__main__':
    N, V = map(int, input().split())
    goods = []
    for i in range(N):
        goods.append(tuple(map(int, input().split())))
    solve(N, V, goods)
