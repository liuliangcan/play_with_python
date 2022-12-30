import sys
from bisect import *
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

# RI = lambda: map(int, sys.stdin.buffer.readline().split())
# RS = lambda: sys.stdin.readline().strip().split()
# RILST = lambda: list(RI())

# input = sys.stdin.buffer.readline
# RI = lambda: map(int, input().split())
# RS = lambda: map(bytes.decode, input().strip().split())
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1494/C

输入 t (≤1000) 表示 t 组数据，每组数据输入 n (≤2e5) m (≤2e5)，长为 n 的严格递增数组 a (-1e9≤a[i]≤1e9) 和长为 m 的严格递增数组 b (-1e9≤b[i]≤1e9)。a 和 b 中均不包含 0。所有数据的 n 之和、m 之和均不超过 2e5。

你在玩一个一维推箱子的游戏，你的初始位置为 0，箱子的位置由数组 a 表示，特殊位置由数组 b 表示。
你可以同时推动多个相邻的箱子。
你不能穿过箱子。
你不能拉箱子。
对于每组数据，输出最多可以让多少个箱子在特殊位置上。
注意可能有的箱子一开始就在特殊位置上。

你能做到线性时间复杂度，且除去输入的空间为常数吗？

输入
5
5 6
-1 1 5 11 15
-4 -3 -2 6 7 15
2 2
-1 1
-1000000000 1000000000
2 2
-1000000000 1000000000
-1 1
3 5
-1 1 2
-2 -1 1 2 5
2 1
1 2
10
输出
4
2
0
3
1
"""


#  推箱子	265  ms
def solve(n, m, a, b):
    bo = bisect_right(a, 0)  # 负坐标箱子数
    po = bisect_right(b, 0)  # 负坐标位置数

    def calc(a, b):  # 只计算正坐标部分，双指针
        n = len(a)
        x = set(a) & set(b)  # 尚未遍历到的位置的交集；遍历过程中把已访问的位置去掉
        ans = len(x)
        j = 0  # a的指针
        cnt_box = 0  # 已访问箱子数
        q = deque()  # 滑窗队列维护已访问相交的特殊位置
        for r in b:  # 遍历位置，同时已访问的相交位置从x中删除
            q.append(r)
            x.discard(r)
            while j < n and a[j] <= r:
                cnt_box += 1
                # if a[j] in x:
                #     x.remove(a[j])
                j += 1
            while q and q[-1] - q[0] + 1 > cnt_box:
                q.popleft()
            ans = max(ans, len(x) + len(q))
        return ans

    # 正负坐标分别算求和
    print(calc(a[bo:], b[po:]) + calc([-a[i] for i in range(bo - 1, -1, -1)], [-b[i] for i in range(po - 1, -1, -1)]))


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        n, m = RI()
        a = RILST()
        b = RILST()
        solve(n, m, a, b)
