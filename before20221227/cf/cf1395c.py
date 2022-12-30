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

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1395/C

输入 n(≤200) 和 m(≤200)，长为 n 的数组 a(0≤a[i]<512) 和长为 m 的数组 b(0≤b[i]<512)。
对于每个 a[i]，你可以选择任意一个 b[j]，组成 c[i]=a[i]&b[j]。
输出 c 数组的所有元素按位或的最小值。 

思考：如果值域是 1e9 要怎么做？
https://codeforces.com/contest/1395/submission/148506798

方法一：暴力枚举

提示 1：枚举答案 ans。

提示 2：这意味着 c[i] | ans = ans。

提示 3：对每个 a[i]，枚举看是否存在 a[j] 使得 (a[i]&a[j]) | ans = ans。

时间复杂度 O(512nm)。

方法二：从高到低逐个考虑每个比特位

如果答案的某个比特位可以是 0，那么需要更新 a[i] 可以选择的 a[j] 的集合。

时间复杂度 O(9nm)。

可以参考 https://www.luogu.com.cn/blog/yltx/solution-cf1395c"""


# 77 贪心 每次取max(min()),然后每个数字减去当前选择的1,nnmlgm
def solve(n, m, a, b):
    q = []
    for v in a:
        q.append(sorted(set(x & v for x in b)))
        if q[-1][0] == 0:
            q.pop()
    ans = 0
    while q:
        mx = 0
        for i, v in enumerate(q):
            if v[0] > q[mx][0]:
                mx = i
        ans |= q[mx][0]
        nq = []
        for i, v in enumerate(q):
            if i == mx:
                continue
            nq.append(sorted(set(x ^ (x & ans) for x in v)))
            if nq[-1][0] == 0:
                nq.pop()
        q = nq

    print(ans)


# 枚举，本题不能二分，因为不连续 512nm
def solve2(n, m, a, b):
    for ans in range(513):
        for i in a:
            for j in b:
                if ans | (i & j) == ans:
                    break
            else:
                break
        else:
            return print(ans)


# 不排序 nnm
def solve2(n, m, a, b):
    ands = []
    for v in a:
        ands.append(set(x & v for x in b))
        if 0 in ands[-1]:
            ands.pop()
    ans = 0
    while ands:
        mx = 0
        mxv = -1
        for i, v in enumerate(ands):
            cv = min(v)
            if cv > mxv:
                mx = i
                mxv = cv
        ans |= mxv
        nq = []
        for i, v in enumerate(ands):
            if i == mx:
                continue
            s = set()
            for x in v:
                if 0 == x ^ (x & ans):
                    break
                s.add(x ^ (x & ans))
            else:
                nq.append(s)
        ands = nq

    print(ans)


#  9nm
def solve3(n, m, a, b):

    def check(cur, offset):
        for i in a:
            for j in b:
                if ((((i >> offset) & (j >> offset)) << offset) | cur) == cur:
                    break
            else:
                return False
        return True

    ans = 0
    for i in range(9, -1, -1):
        if not check(ans, i):
            ans |= 1 << i

    print(ans)


if __name__ == '__main__':
    n, m = RI()
    a = RILST()
    b = RILST()

    solve(n, m, a, b)
