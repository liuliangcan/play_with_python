# Problem: F - Ignore Operations
# Contest: AtCoder - Monoxer Programming Contest 2022（AtCoder Beginner Contest 249）
# URL: https://atcoder.jp/contests/abc249/tasks/abc249_f
# Memory Limit: 1024 MB
# Time Limit: 2000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

import sys
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
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc249/tasks/abc249_f

初始时 x=0。
输入 n k(k≤n≤2e5)，以及 n 个操作，每个操作是如下两种之一：
"1 y"，表示把 x 替换成 y；
"2 y"，表示 x+=y。(-1e9≤y≤1e9)
你可以跳过至多 k 个操作，你需要最大化最后的 x，输出这个最大值。
输入 
5 1
2 4
2 -3
1 2
2 1
2 -3
输出 3
解释 跳过最后一个

输入 
1 0
2 -1000000000
输出 -1000000000

https://atcoder.jp/contests/abc249/submissions/37631511

提示 1：由于操作 1 会覆盖之前的所有操作，因此倒序思考这些操作更合适。

提示 2：假设某个操作 1 是最后一次操作 1，那么在它之后的操作 1 都应该 skip。

提示 3：如果 skip 的操作达到了 k，后面又遇到了操作 2，那么我们应该「撤销」之前的 skip，也就是把最大的负数 y 撤销掉（绝对值最小的 y）。

提示 4：用堆来实现。（这个套路也叫反悔堆）

代码实现时可以在最前面插入一个 "1 0" 方便统一操作。
"""
"""这题想到逆序处理等于过了一半
    修改后，操作的形状一定是
            ....122222222
    即从后边选择k个1和2跳过，最后留下的操作中，尾巴拥有连续的操作2
    因为只有跳过了1，更前边的操作2跳过才有意义：换句话说，从留下的操作1前边选操作2跳过是无意义的。
"""


#  267   ms
def solve():
    n, k = RI()
    x, bad, ops = 0, [], [(1, 0)]  # x,需跳过的op2,ops实现补个(1,0)方便操作
    for _ in range(n):
        op, y = RI()
        if op == 1:
            x, y = y, y - x  # 把y处理为本次操作的改变值
        else:
            x += y
        ops.append((op, y))

    f = fix1 = fix2 = 0  # 跳过的操作1和操作2对答案的贡献
    for op, y in ops[::-1]:
        if op == 1:  # 操作1必须跳过，否则后边的操作2修改都没有意义
            if fix1 + fix2 < f:  # 只在遇到操作1的时候更新答案即可，由于实现填充了(1,0)，因此保证至少可以更新一次答案
                f = fix1 + fix2
            if k == 0:
                break
            k -= 1  # 留给操作2的机会不多了
            fix1 += y
        else:
            if y < 0:  # 操作2只选择负数跳过
                heappush(bad, -y)
                fix2 += y
        while len(bad) > k:  # 容量外的操作2干掉
            fix2 += heappop(bad)

    print(x - f)


#   264  ms
def solve1():
    n, k = RI()
    x, bad, ops = 0, [], []
    for _ in range(n):
        op, y = RI()
        if op == 1:
            x, y = y, y - x  # 把y处理为本次操作的改变值
        else:
            x += y
        ops.append((op, y))

    f = fix1 = fix2 = 0  # 跳过的操作1和操作2对答案的贡献
    for op, y in ops[::-1]:
        if k == 0:
            break
        if op == 1:  # 操作1必须跳过，否则后边的操作2修改都没有意义
            k -= 1  # 留给操作2的机会不多了
            fix1 += y
        else:
            if y < 0:  # 操作2只选择负数跳过
                heappush(bad, -y)
                fix2 += y
        while len(bad) > k:  # 容量外的操作2干掉
            fix2 += heappop(bad)
        if fix1 + fix2 < f:
            f = fix1 + fix2

    print(x - f)


if __name__ == '__main__':
    solve()
