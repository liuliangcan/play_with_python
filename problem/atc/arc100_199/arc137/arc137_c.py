# Problem: C - Distinct Numbers
# Contest: AtCoder - AtCoder Regular Contest 137
# URL: https://atcoder.jp/contests/arc137/tasks/arc137_c
# Memory Limit: 1024 MB
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
PROBLEM = """https://atcoder.jp/contests/arc137/tasks/arc137_c

输入 n(2≤n≤3e5) 和长为 n 的严格递增数组 a(0≤a[i]≤1e9)。

Alice 和 Bob 在玩一个回合制游戏，Alice 先手。
游戏规则如下：
1. 一开始，数轴上有 n 颗石子，第 i 颗石子的位置是 a[i]。
2. 每个回合，玩家只能移动最右边的那颗石子。且必须将它移动到在它左边的没有石子的非负整数空位上。例如 a=[2,4]，你只能移动位置 4 上的石子到位置 0 或 1 或 3。
3. 移动石子后，轮到另一个玩家继续移动这 n 颗石子中的最右边的石子。如此交替。
4. 无法移动的玩家输掉游戏，另一位玩家获胜。

如果 Alice 必胜，输出 Alice，否则输出 Bob。
输入 
2
2 4
输出 Alice
解释 Alice 把 4 移动到 3，就可以保证必胜。（手玩一下）

输入 
3
0 1 2
输出 Bob
"""
"""设x,y = n-2,n-1

根据游戏规则的不同情况，得出了以下结论：

情况一：如果最右边的两个石子之间有空位，即 a[x+1] < a[y]
    Alice尝试把y移动到x+1,则Bob需要把x+1移动到一个比x小的位置，有两种情况：
        - bob没有必胜策略，则alice胜
        - bob移动到z必胜，则alice悔棋，第一步直接移动到z，则alice胜
即如果最右边的两个石子之间有空位，即 a[x+1] < a[y]，那么 Alice 必胜。

情况二：如果最右边的两个石子之间没有空位，即 a[x+1] = a[y]。
通过情况1我们知道，如果某一步移动后，最后两个石子之间有空位，当前人是必胜的；因此最优策略一定要保证每次移动完，最后俩位置没有空位。
那么每次移动，max(a)只会减小1.
游戏结束时max(a)=n-1,所以一共有y-(n-1)个回合。如果是奇数 Alice胜，否则bob胜。 
 """


#       ms
def solve():
    n, = RI()
    a = RILST()
    x, y = a[-2:]
    if x + 1 < y or (y - n) % 2 == 0:
        print('Alice')
    else:
        print('Bob')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
