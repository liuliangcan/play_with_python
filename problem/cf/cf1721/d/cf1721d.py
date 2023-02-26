# Problem: D. Maximum AND
# Contest: Codeforces - Educational Codeforces Round 134 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1721/D
# Memory Limit: 256 MB
# Time Limit: 3000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf, comb
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1721/D

输入 t(≤1e4) 表示 t 组数据，每组数据输入 n(≤1e5) 和两个长为 n 的数组 a b，元素范围在 [0,2^30)。所有数据的 n 之和不超过 1e5。

数组 b 可以随意打乱。
输出 (a[1] XOR b[1]) AND (a[2] XOR b[2]) AND ... AND (a[n] XOR b[n]) 的最大值。
输入
3
5
1 0 0 3 3
2 3 2 1 0
3
1 1 1
0 0 3
8
0 1 2 3 4 5 6 7
7 6 5 4 3 2 1 0
输出
2
0
7
https://codeforces.com/contest/1721/submission/189632358

提示 1：从最高位往最低位一位一位思考。

提示 2：a 中的 0 需要和 b 中的 1 匹配，a 中的 1 需要和 b 中的 0 匹配。

提示 3：如果可以匹配，则分组，问题规模缩小，可以用递归来思考更低位的匹配。
但是，如果当前位的任意一个子问题匹配失败，则对于这个位，所有匹配都是无效的（因为算的是 AND）。此时应该跳过这个位上的所有匹配，直接计算下一个更低位的匹配。

提示 4：用 BFS+双数组，从而能实现这个跳过的逻辑。
匹配失败时，直接还原回原来的数组。具体见代码。
"""

"""对于每一位，必须使a中1对应b中0，a中0对应b中1，它们对应的数量应该一致。且不破坏上一个高位。
考虑第一位，a中的1可以对应b中0任意一个书，a中0同理。那么把数据分成两组(a0,b1),(a1,b0)。
考虑第二位，不破坏上一位的前提下，刚才的组只能组内对应，即a00对应b01,a01对应b00，因此分成4组(a00,b11),(a01,b10),(a10,b01),(a11,b00)
考虑第三位，同理分8组(a000,b111),(a001,b110),,(a010,b101),(a011,b100),,(a100,b011),(a101,b010),,(a110,b001),(a111,b000)
..

对于每一位，只要任意一组分不成功，则本位一定是0，答案(位与)的本位就是0。即需要保证每组都能分上，才是1。
如果分不成功，可以直接跳到分析下一位，而且是从上一位的状态开始转移，因为本位随便分反正都是0。
这里由于q是整体必须全部通过，而且可能需要整体还原，因此直接用数组遍历即可。

因此这里状态是指q数组本身的整体状态：并非队列中存多个状态，而是队列本身整体是一个状态。区别于通常的BFS
每次状态转移实际上是有唯一的一种分组情况(即使组内随便对应)，状态的总数据量不变，即状态数不会变多，单个状态也不会变大。
"""


#  982      ms
def solve1():
    n, = RI()
    a = RILST()
    b = RILST()
    ans = 0
    q = [(a, b)]  # ab当前元素的分组状态,每个ab代表随便a中任意对应b中任意

    for k in range(29, -1, -1):
        t, q = q, []
        for a, b in t:
            f, g = [[], []], [[], []]
            for v in a:  # a中对应位归纳
                f[(v >> k) & 1].append(v)
            for v in b:  # b中对应位归纳
                g[(v >> k) & 1].append(v)
            if len(f[0]) != len(g[1]):  # 01数量不同则在这个ab组内无法让这位异或为1了
                q = t  # 还原到上一位的状态
                break
            if f[0]:  # 分出来的第一组
                q.append((f[0], g[1]))
            if f[1]:  # 分出来的第二组
                q.append((f[1], g[0]))
        else:  # 本位可以完成分组,q变成了新的
            ans |= 1 << k

    print(ans)


#    592    ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    ans = 0

    def ok(mask):
        cnt = Counter()
        for v in a:
            cnt[v & mask] += 1
        for v in b:
            cnt[~v & mask] -= 1
        return all(v == 0 for v in cnt.values())

    for k in range(29, -1, -1):
        if ok(ans | (1 << k)):
            ans |= 1 << k

    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
