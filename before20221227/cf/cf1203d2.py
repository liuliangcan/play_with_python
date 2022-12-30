import os
import sys
from math import floor, ceil

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 998244353


def solve(s, t):
    n, m = len(s), len(t)
    f, g = [0] * n, [0] * n
    j = m - 1
    for i in range(n - 1, -1, -1):
        if j >= 0 and s[i] == t[j]:
            j -= 1
        f[i] = m - j - 1
    f = f[:1] + f + [0]
    j = 0
    for i in range(n):
        if j < m and s[i] == t[j]:
            j += 1
        g[i] = j
    g = [0] + g + g[-1:]
    # print(g, f)
    ans = 0
    j = 0
    for i in range(n + 2):
        while j < n + 2 and g[i] + f[j] == m:
            ans = max(ans, j - i - 1)
            j += 1

    print(ans)


if __name__ == '__main__':
    s = input()
    t = input()
    solve(s, t)
    a = 1
    b = a2
