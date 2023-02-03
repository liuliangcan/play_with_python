# Problem: F - Best Concatenation
# Contest: AtCoder - UNIQUE VISION Programming Contest 2022 Summer (AtCoder Beginner Contest 268)
# URL: https://atcoder.jp/contests/abc268/tasks/abc268_f
# Memory Limit: 1024 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import sys
import heapq
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc268/tasks/abc268_f

输入 n(≤2e5) 和 n 个字符串，总长度不超过 2e5。
每个字符串包含 X 和数字 1~9。
重排这些字符串，然后拼接成一个字符串 t。
对每个 1≤i<j≤len(t)，如果 t[i]=X 且 t[j]=1 则得 1 分，如果 t[i]=X 且 t[j]=2 则得 2 分，依此类推。
输出你最多可以得到多少分。
输入
3
1X3
59
XXX
输出 71
解释 t=XXX1X359
"""
"""贪心，最优解有严格的顺序，用邻项交换法考虑
假设两项a b中x的数量和数值总和分别是xa sa xb sb ，以及它们本身对答案的贡献是pa,pb，显然，本身的贡献是固定的，不用考虑
则
    ab对答案的其余贡献是xa*sb
    ba对答案的其余贡献是xb*sa
    令ba>ab,即 
        xb*sa > xa*sb
        sa/xa > sb/xb
    即x/s大的后访问，小的先访问               
"""
# 254
if __name__ == '__main__':
    n, = RI()
    a = []
    b = []
    ans = 0
    for _ in range(n):
        w, = RS()
        s = x = 0
        for c in w:
            if c == 'X':
                x += 1
            else:
                ans += x * int(c)
                s += int(c)
        if s:
            a.append((x, s))
        else:
            b.append((x, 0))
    p = 0
    for x, s in sorted(a, key=lambda x: x[0] / x[1]) + b:
        ans += p * x
        p += s
    print(ans)

# # 258
# if __name__ == '__main__':
#     n, = RI()
#     a = []
#     ans = 0
#     for _ in range(n):
#         w, = RS()
#         s = x = 0
#         for c in w:
#             if c == 'X':
#                 x += 1
#             else:
#                 ans += x * int(c)
#                 s += int(c)
#         a.append((x, s))
#     a.sort(key=lambda x: x[0] / x[1] if x[1] else inf)
#     p = 0
#     for x, s in a:
#         ans += p * x
#         p += s
#     print(ans)

# # 377
# if __name__ == '__main__':
#     n, = RI()
#     a = []
#     ans = 0
#     for _ in range(n):
#         w, = RS()
#         s = x = 0
#         for c in w:
#             if c == 'X':
#                 x += 1
#             else:
#                 ans += x*int(c)
#                 s += int(c)
#         a.append(((x / s if s else inf), x, s))
#     a.sort()
#     p = 0
#     for _, x, s in a:
#         ans += p * x
#         p += s
#     print(ans)

# # 398
# if __name__ == '__main__':
#     n, = RI()
#     a = []
#     ans = 0
#     for _ in range(n):
#         w, = RS()
#         s = x = 0
#         for c in w[::-1]:
#             if c == 'X':
#                 ans += s
#                 x += 1
#             else:
#                 s += int(c)
#         a.append(((x / s if s else inf), x, s))
#     a.sort()
#     p = 0
#     for _, x, s in a:
#         ans += p * x
#         p += s
#     print(ans)
