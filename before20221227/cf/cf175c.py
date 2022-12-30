import collections
import os
import sys
from collections import Counter
# print(sys.hexversion)
# if os.getenv('LOCALCFTEST'):
#     sys.stdin = open('abcinput.txt')
# else:
#     input = sys.stdin.readline
if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
else:
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


def solve(n, kc, t, p):
    kc.sort(key=lambda x: x[1])
    p.append(10 ** 18)
    ans = 0
    s = 0  # 当前杀怪总数
    j = 0
    for k, c in kc:
        while s + k >= p[j]:  # 如果k能覆盖当前组j就计算j组，消耗k，步进总数
            ans += (p[j] - s) * c * (j + 1)
            k -= p[j] - s
            s = p[j]
            j += 1
        ans += k * c * (j + 1)  # k无法覆盖，则消耗完k，步进总数
        s += k
    print(ans)


if __name__ == '__main__':
    n = int(input())
    kc = []
    for _ in range(n):
        kc.append(list(map(int, input().split())))
    t = int(input())
    p = list(map(int, input().split()))
    solve(n, kc, t, p)
