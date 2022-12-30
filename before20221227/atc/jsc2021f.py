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
"""https://atcoder.jp/contests/jsc2021/tasks/jsc2021_f

输入 n m q (≤2e5)，初始你有长为 n 的数组 a，长为 m 的数组 b，元素值都为 0，下标从 1 开始。
然后输入 q 个询问，每个询问形如 t x y (1≤y≤1e8)。
t=1，表示把 a[x]=y；t=2，表示把 b[x]=y。
每次修改后，输出 ∑∑max(a[i],b[j])，这里 i 取遍 [1,n]，j 取遍 [1,m]。
输入
2 2 4
1 1 10
2 1 20
2 2 5
1 1 30
输出
20
50
55
85

输入
3 3 5
1 3 10
2 1 7
1 3 5
2 2 10
2 1 1
输出
30
44
31
56
42

输入
200000 200000 4
2 112219 100000000
1 73821 100000000
2 26402 100000000
1 73821 100000000
输出
20000000000000
39999900000000
59999800000000
59999800000000
"""


class BinIndexTree:
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            i &= i - 1
        return s

    def lowbit(self, x):
        return x & -x


""" 思路:q<2e5,显然复杂度要控制在qlgX以内,考虑每次答案从上一次状态转化。
考虑变更a[i]位置的值从x到y。
由于a中其它位置不变，因此其它位置对答案求和的贡献也不变。
减去上次x贡献了答案的部分;再加上y对本次答案的贡献就是本次答案。
如何计算x或y对答案的贡献呢:sum(max(x,z)|z∈b)。
我们可以把b中的数分为两部分:
    1) z<=x的数,他们求max(z,x)=x,对答案的贡献+=x*cnt(z|z∈b,z<=x)
    2) z>x的数,他们求max(z,x)=z,对答案的贡献+=sum(z|z∈b,z>x)
以上两部分不重不漏的可以计算x对答案的贡献。
因此需要快速计算b中小于特定数的值个数cnt、大于特定数的值求和sum。
这两个操作都可以用`值域树状数组`lg代价计算。
由于题目操作是赋值set=，因此值域就是set的值最大值1e8，离散化成2e5即可。注意初始态是0，记得加。如果不能离散化需要动态开点线段树。
复杂度O(qlgV),其中V是询问中set的值的去重计数,显然V<=q。
实现时，操作a和b是对称的，因此可以用数组组合两边的数据结构，用下标t^1(or 1-t)来获取当前组和对面组(这里t从1开始，可以2-t)

扩展:如果题目里的操作改成a[x]+=y,其实也不用动态开点线段树。
可以实现从头到尾模拟一遍q的操作，记录所有a[x]的结果，就是值域了，依然可以离散化。
"""


#    932   	 ms
def solve(n, m, q, qs):
    ab = [[0] * n, [0] * m]  # a\b数组，用数组组合起来，减小代码量方便码。
    hs = sorted({x for _, _, x in qs} | {0})  # 离散化
    sz = len(hs)
    trees = [[BinIndexTree(sz), BinIndexTree(sz)] for _ in range(2)]  # 两边分别有2颗树，分别记录本数组每个值数量和数值和
    trees[0][0].add_point(1, n)  # 初始，a所有数都是0，因此数量在0上有n个;b同理
    trees[1][0].add_point(1, m)
    ret, ans = 0, []
    for t, i, y in qs:
        a = ab[t - 1]  # 当前数组
        x, a[i - 1] = a[i - 1], y  # x,y分别是老值新值
        xx = bisect_left(hs, x) + 1
        yy = bisect_left(hs, y) + 1

        cnt, sum = trees[t - 1]  # 在自己的树做变更
        cnt.add_point(xx, -1)  # x位置少一个数
        cnt.add_point(yy, +1)  # y位置多一个数
        sum.add_point(xx, -x)  # x位置上和减小
        sum.add_point(yy, +y)  # y位置上和增加

        cnt, sum = trees[2 - t]  # 去对面那棵树算变化
        ret -= cnt.sum_prefix(xx) * x + sum.sum_interval(xx + 1, sz)  # 小于x的max是x，贡献是cnt*x；大于x的max是z，贡献是sum(z)
        ret += cnt.sum_prefix(yy) * y + sum.sum_interval(yy + 1, sz)
        ans.append(ret)
        # print(ab)
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    n, m, q = RI()
    qs = []
    for _ in range(q):
        qs.append(RILST())

    solve(n, m, q, qs)
    x = 2+4+7*2+7*7*4+7*7*7*4 +7*7*7*7*4
    print(x)