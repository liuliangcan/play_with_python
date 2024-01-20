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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/contest/1701/problem/C

输入 T(≤1e4) 表示 T 组数据。所有数据的 m 之和 ≤2e5。
每组数据输入 n m(1≤n≤m≤2e5) 和长为 m 的数组 a(1≤a[i]≤n)。

有 n 名工人和 m 个任务，a[i] 表示擅长第 i 个任务的工人编号。
每个任务只能分配给一名工人。如果工人擅长该任务，他会用 1 小时完成，否则需要 2 小时完成。
一名工人一次只能做一个任务，完成一个任务后，才能开始他的下一个任务。
所有工人同时开始工作。

输出完成所有任务最少要多少小时。
输入
4
2 4
1 2 1 2
2 4
1 1 1 1
5 5
5 1 3 2 4
1 1
1
输出
2
3
1
1 
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


#       ms
def solve():
    n, m = RI()
    a = RILST()
    good = [0] * n
    for v in a:
        good[v - 1] += 1

    def ok(x):
        task1 = 0
        task2 = 0
        for v in good:
            if v <= x:
                task1 += v
                task2 += (x-v)//2
            else:
                task1 += x
        return task1 + task2 >= m
    # print(ok(3))

    print(lower_bound(0, m * 2 + 1, ok))


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
