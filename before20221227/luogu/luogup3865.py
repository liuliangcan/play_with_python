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
from operator import or_

if sys.hexversion == 50923504:
    sys.stdin = open('cfinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://www.luogu.com.cn/problem/P3865
st求区间max模板题
"""


class SparseTable:
    def __init__(self, data: list, func=or_):
        # 稀疏表，O(nlgn)预处理，O(1)查询区间最值/或和/gcd
        # 下标从0开始
        self.func = func
        self.st = st = [list(data)]
        i, N = 1, len(st[0])
        while 2 * i <= N:
            pre = st[-1]
            st.append([func(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)])
            i <<= 1

    def query(self, begin: int, end: int):  # 查询闭区间[begin, end]的最大值
        lg = (end - begin+1).bit_length() - 1
        return self.func(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])



if __name__ == '__main__':
    n, m = RI()
    st = SparseTable(RILST(), max)

    for _ in range(m):
        l, r = RILST()
        print(st.query(l - 1, r - 1))
