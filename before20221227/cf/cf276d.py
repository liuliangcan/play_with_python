import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

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
"""https://codeforces.com/problemset/problem/276/D

输入 L 和 R (1≤L≤R≤1e18)。
输出区间 [L,R] 内任意两个数的异或的最大值。

思考题：如果还要求异或不超过某个 limit 呢？

输入 1 2
输出 3

输入 8 16
输出 31

输入 1 1
输出 0
https://codeforces.com/contest/276/submission/118793107

如果 L 和 R 的二进制长度不一样，例如 L=2，R=9，那么我们可以用 7^8 得到最大的异或和 15。

推广，如果 L 和 R 的二进制长度一样，那么我们可以从高到低找到第一个二进制不同的位置，转换到长度不一样的情况。

总之，答案为 (1 << bit_length(L ^ R)) - 1。

思考题代码 https://github.com/EndlessCheng/codeforces-go/blob/master/copypasta/bits.go#L632
"""


#  	 ms
def solve(l, r):
    print((1 << (l ^ r).bit_length()) - 1)


if __name__ == '__main__':
    l, r = RI()

    solve(l, r)
