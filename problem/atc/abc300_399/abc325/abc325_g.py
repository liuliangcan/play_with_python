# Problem: G - offence
# Contest: AtCoder - KEYENCE Programming Contest 2023 Autumn（AtCoder Beginner Contest 325）
# URL: https://atcoder.jp/contests/abc325/tasks/abc325_g
# Memory Limit: 1024 MB
# Time Limit: 2000 ms


#       ms
from math import inf
"""区间DP
定义f[i][j]为这个区间的最少字符。
f[i][j]=0则表示这段可以完整删除。
遇到of和中间是0的情况，则可以向后删除k个，但这k个可能已经被删过，要用f[r+1][x]<=k来判断这段能不能删到
注意可以提前处理f[i][i]=1；i>j的都是0。或者一边转移一边处理也行
"""

def solve():
    s = input()
    k = int(input())
    n = len(s)
    f = [[inf] * n for _ in range(n)]
    for i in range(n):
        f[i][i] = 1
        for j in range(n):
            if i > j:
                f[i][j] = 0
    for l in range(n - 1, -1, -1):
        for r in range(l + 1, n):
            for i in range(l, r):
                f[l][r] = min(f[l][r], f[l][i] + f[i + 1][r])
            if s[l] == 'o' and s[r] == 'f' and f[l + 1][r - 1] == 0:
                f[l][r] = 0
                for x in range(n):
                    if r + x >= n:
                        break
                    if r + 1 < n and f[r + 1][r + x] <= k:
                        f[l][r + x] = 0

    print(f[0][n - 1])


if __name__ == '__main__':
    solve()
