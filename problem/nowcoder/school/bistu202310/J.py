# Problem: 小苯选择队友
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/65319/J
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """对每种数字分组，单独讨论。
1. 现在讨论值=v的数字，他们的下标分别是[i0,i1,i2..ik]
2. 左右端点一定在这里边，否则一定可以收缩端点使和变大。
3. 这些下标中间的数都是负贡献，可以合并成一个数。（用前缀和优化
4. 那么就变成最大子段和问题，记得储存下标就行。（注意题面拉到最后有额外条件
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    ans = [0, 0, -1, -1]  # 和(记相反数取小方便处理答案), k, l, r
    pre = [0] + list(accumulate(a))
    pos = defaultdict(list)
    for i, v in enumerate(a):
        pos[v].append(i)
    for v, ps in pos.items():  # 一起比较就不用排序了
        s = 0  # 段和
        i0 = ps[0]  # 起点
        p = ps[0] - 1  # 前个下标
        for i in ps:
            s -= pre[i + 1 - 1] - pre[p + 1]  # 减去中间的敌人
            if s < 0:  # l要优先取小的，那么前边的0不能丢
                i0 = i
                s = a[i]
            else:
                s += a[i]
            p = i
            if [-s, v, i0 + 1, i + 1] < ans:  # 更新答案，注意都要取小的
                ans = [-s, v, i0 + 1, i + 1]

    print(*ans[1:])


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
