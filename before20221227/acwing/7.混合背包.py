import io
import os
import sys
from collections import deque

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve(N, V, goods):
    dp = [0] * (V + 1)

    def zero_one_pack(v, w):
        for j in range(V, v - 1, -1):
            dp[j] = max(dp[j - v] + w, dp[j])

    def complete_pack(v, w):
        for j in range(v, V + 1):
            dp[j] = max(dp[j - v] + w, dp[j])

    def multi_pack(v, w, s):
        if v * s >= V:
            return complete_pack(v, w)
        pre = dp[:]
        for k in range(v):
            q = deque()
            for j in range(k, V + 1, v):
                if q and q[0] < j - s * v:
                    q.popleft()
                while q and pre[q[-1]] + (j - q[-1]) // v * w <= pre[j]:
                    q.pop()
                q.append(j)
                dp[j] = pre[q[0]] + (j - q[0]) // v * w

    for v, w, s in goods:
        if s == 0:
            complete_pack(v, w)
        elif s == -1 or s == 1:
            zero_one_pack(v, w)
        else:
            multi_pack(v, w, s)
    print(dp[V])


if __name__ == '__main__':
    N, V = map(int, input().split())
    goods = []
    for i in range(N):
        goods.append(tuple(map(int, input().split())))
    solve(N, V, goods)
