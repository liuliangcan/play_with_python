# Problem: D. Professor Higashikata
# Contest: Codeforces - Codeforces Round 882 (Div. 2)
# URL: https://codeforces.com/contest/1847/problem/D
# Memory Limit: 256 MB
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
PROBLEM = """该问题是一个关于二进制字符串的竞争编程问题。给定一个长度为n的二进制字符串s，定义操作为选择两个不同的整数i和j（1≤i<j≤n），并交换字符si和sj。

问题要求对字符串进行q次更新。在第i次更新中，将第sxi个字符翻转，即如果sxi=1，则变为0，反之亦然。在每次更新后，需要找到使得t(s)（按照一定顺序拼接的子字符串）在字典序上尽可能大的最小操作次数。

需要注意的是，实际上并不执行任何操作，只关心操作的次数。

输入部分包括三个整数n、m和q，分别表示字符串长度、子字符串数量和更新次数。接下来一行是长度为n的二进制字符串s。接下来的m行中，每行包含两个整数li和ri，表示子字符串的起始位置和结束位置。接下来的q行中，每行包含一个整数xi，表示要进行更新的位置。

输出部分需要打印q个整数，其中第i个整数表示在第i轮中，需要进行的最小操作次数，以使得t(s)在字典序上尽可能大。
输入：
2 2 4
01
1 2
1 2
1
1
2
2
输出：
0
1
0
1
"""
"""乔瑟克厌倦了他在莫里奥的平静生活。他决定效仿侄子乔塔洛的脚步，努力学习并成为一名计算机科学教授。在网上寻找竞争编程问题时，他遇到了以下问题：

设s为长度为n的二进制字符串。对s的操作定义为选择两个不同的整数i和j（1≤i<j≤n），并交换字符si和sj。

考虑字符串t1,t2,…,tm，其中ti是s从li到ri的子字符串。定义t(s)=t1+t2+…+tm为按照这种顺序连接字符串ti得到的字符串。

对字符串进行q次更新。第i次更新中，将第sxi个字符翻转。即如果sxi=1，则变为0，反之亦然。每次更新后，找到使得t(s)在字典序上尽可能大的最小操作次数。

请注意，实际上并不执行任何操作，我们只关心操作的次数。

通过解决这个问题，帮助乔瑟克实现他的梦想。

——————————————————————

字符串a是字符串b的子串，如果a可以通过从b的开头删除零个或多个字符以及从末尾删除零个或多个字符得到。

如果字符串a和字符串b的长度相同，且在第一个不同的位置上，字符串a有一个1，而字符串b有一个0，则字符串a在字典序上大于字符串b。

输入部分包含三个整数n、m和q，分别表示字符串的长度、子字符串的数量和更新次数。接下来一行是长度为n的二进制字符串s。接下来的m行中，每行包含两个整数li和ri，表示子字符串的起始位置和结束位置。接下来的q行中，每行包含一个整数xi，表示要进行更新的位置。

输出部分需要打印q个整数，其中第i个整数表示在第i轮中，需要进行的最小操作次数，以使得t(s)在字典序上尽可能大。"""
"""链式并查集+树状数组
首先找到所有目标范围是m个区间，但是这里有重复的，显然，可以贪心的只考虑它第一次出现的位置。
    - 那么这里用链式并查集，把所有目标位置一个一个找出来，从并查集里移除。复杂度O(n)
    - 注意记录顺序。
然后考虑要让目标区间最大，显然是尽可能的把前边填上1。假设区间大小为size，s中一共p个1。那么区间内最多能放x=min(size,p)个1。
    - 那么把这x个1放到目标区间的前x个位置即可，显然，本来就是1的地方不用动，那么要动的地方就是目标区间前x个位置里的0。
    - 那么0的个数就是答案。
    - 可以用树状数组求出1的个数v，ans=x-v
- 额外的工作就是实时记录原串s上1的总个数即可。
"""

#   467    ms
def solve():
    n, m, q = RI()
    s, = RS()
    s = list(map(int, s))
    fa = list(range(n + 1))

    def find(x):
        t = x
        while fa[x] != x:
            x = fa[x]
        while t != x:
            t, fa[t] = fa[t], x
        return x

    def union(x, y):
        x, y = find(x), find(y)
        fa[x] = y

    order = []  # 用链式并查集找到每个目标位置和顺序
    for _ in range(m):
        l, r = RI()
        l -= 1
        r -= 1
        l = find(l)
        while l <= r:
            order.append(l)
            union(l, l + 1)
            l = find(l)
    ss = sum(s)  # 总共有多少个1
    size = len(order)
    c = [0] * (size + 1)

    # print(order)
    def add(i, v=1):
        while i <= size:
            c[i] += v
            i += i & -i

    def query(i):
        s = 0
        while i:
            s += c[i]
            i -= i & -i
        return s

    st = [0]*n
    for i, v in enumerate(order, start=1):
        if s[v]:
            add(i)
        st[v] = i

    for _ in range(q):
        pos, = RI()
        pos -= 1
        s[pos] ^= 1
        ss += 1 if s[pos] else -1
        if st[pos]:
            add(st[pos], 1 if s[pos] else -1)
        p = min(ss, size)
        print(p - query(p))


#   546    ms
def solve1():
    n, m, q = RI()
    s, = RS()
    s = list(map(int, s))
    fa = list(range(n + 1))

    def find(x):
        t = x
        while fa[x] != x:
            x = fa[x]
        while t != x:
            t, fa[t] = fa[t], x
        return x

    def union(x, y):
        x, y = find(x), find(y)
        fa[x] = y

    order = []  # 用链式并查集找到每个目标位置和顺序
    for _ in range(m):
        l, r = RI()
        l -= 1
        r -= 1
        l = find(l)
        while l <= r:
            order.append(l)
            union(l, l + 1)
            l = find(l)
    st = {v: i for i, v in enumerate(order)}  # 转set
    ss = sum(s)  # 总共有多少个1
    size = len(order)
    c = [0] * (size + 1)

    # print(order)

    def add(i, v=1):
        while i <= size:
            c[i] += v
            i += i & -i

    def query(i):
        s = 0
        while i:
            s += c[i]
            i -= i & -i
        return s

    for i, v in enumerate(order, start=1):
        if s[v]:
            add(i)

    for _ in range(q):
        pos, = RI()
        pos -= 1
        s[pos] ^= 1
        ss += 1 if s[pos] else -1
        if pos in st:
            add(st[pos] + 1, 1 if s[pos] else -1)
        p = min(ss, size)
        print(p - query(p))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
