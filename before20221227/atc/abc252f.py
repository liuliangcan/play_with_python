import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc252/tasks/abc252_f

输入 n (2≤n≤2e5) 和 L(≤1e15)，长为 n 的数组 a (1≤a[i]≤1e9, sum(a)≤L)。
有一根长为 L 的面包，需要分给 n 个小孩，每个小孩需要长度恰好为 a[i] 的面包。
对于任意一根长为 k 的面包，你可以切成两段，要求每段长度都为整数，切的花费为 k。
输出最小花费。
输入
5 7
1 2 1 2 1
输出 16

输入
3 1000000000000000
1000000000 1000000000 1000000000
输出 1000005000000000
https://atcoder.jp/contests/abc252/submissions/36006064

逆向思维，把分割看成合并。这样就转换成经典的 Huffman 问题，用最小堆实现。
如果 sum(a) < L，可以把多余的面包额外当成一个小孩需要的。
即：最短的最后切，假设最短的是a、b 和c=a+b，那么a将在切c时出现，花费是c。
然后考虑c什么时候出现，这是个子问题。把c加回heap中。
利用Huffman的满二叉树性质，自低向上构造。
"""


#   340   	 ms
def solve(n, L, a):
    s = L - sum(a)
    if s:
        a.append(s)
    heapq.heapify(a)
    ans = 0
    while len(a) > 1:
        mn = heapq.heappop(a)
        ans += a[0] + mn
        heapq.heapreplace(a, a[0] + mn)

    print(ans)


if __name__ == '__main__':
    n, L = RI()
    a = RILST()

    solve(n, L, a)
