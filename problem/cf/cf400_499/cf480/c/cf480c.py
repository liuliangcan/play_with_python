# Problem: C. Riding in a Lift
# Contest: Codeforces - Codeforces Round 274 (Div. 1)
# URL: https://codeforces.com/contest/480/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from itertools import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/480/problem/C

输入整数 n a b k (2≤n≤5000, 1≤k≤5000, 1≤a,b≤n, a≠b)。
你需要从数轴上的 a 出发，移动恰好 k 次。
从整数 x 移动到整数 y，必须满足以下所有要求：
1. 1≤y≤n
2. y≠x
3. y≠b
4. |x-y|<|x-b|
输出不同移动方案的个数，模 1e9+7。
输入 5 2 4 1
输出 2

输入 5 2 4 2
输出 2

输入 5 3 4 1
输出 0
"""
"""https://codeforces.com/contest/479/submission/208670481

前缀和优化 DP。

为方便计算，如果 a>b，根据对称性调整为 a=n+1-a，b=n+1-b。这样可以保证 a<b。

定义 f[i][j] 表示 i 次移动后，移动到 j 的方案数。f[0][a] = 1。1≤j<b。
考虑从位置 x 转移过来：
如果 x<j，可以移动到 j。
如果 x>j，根据要求 4，解不等式得 x≤j+floor((b-y-1)/2)。
所以 f[i][j] = f[i-1][1] + ... + f[i-1][j+floor((b-y-1)/2)] - f[i-1][j]。
最后的减法是因为要求 2。
答案为 sum(f[k][j])。

用前缀和优化即可做到 O(kb) 的时间复杂度。

代码实现时，f 的第一个维度可以优化掉。

相似题目见右。"""


class BinIndexTree:
    """    PURQ的最经典树状数组，每个基础操作的复杂度都是logn；如果需要查询每个位置的元素，可以打开self.a    """

    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            # self.a = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            # self.a = [0 for _ in range(self.size + 5)]
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        # self.a[i] += v
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    # def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
    #     self.add_point(i, v - self.a[i])
    #     self.a[i] = v

    def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
        if l > r:
            return 0
        return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            # i -= i&-i
            i &= i - 1
        return s

    def __repr__(self):
        return [self.sum_interval(i, i) for i in range(1, self.size + 1)]

    def __str__(self):
        return str(self.__repr__())

    def min_right(self, i):
        """寻找[i,size]闭区间上第一个正数(不为0的数),注意i是1-indexed。若没有返回size+1;复杂度O(lgnlgn)"""
        p = self.sum_prefix(i)
        if i == 1:
            if p > 0:
                return i
        else:
            if p > self.sum_prefix(i - 1):
                return i

        l, r = i, self.size + 1
        while l + 1 < r:
            mid = (l + r) >> 1
            if self.sum_prefix(mid) > p:
                r = mid
            else:
                l = mid
        return r

    def lowbit(self, x):
        return x & -x


"""这样没法优化，交换ij的定义
定义f[i][j]为从i出发，移动j次的方案数
初始:f[b][i] = 0 ,f[i][0] = 1
f[i][j] = sum(f[p][j-1]),p∈[i-d+1,i+d-1],d=abs(b-i)
"""
"""
定义:f[i][j]为从j出发，移动i次的方案数。
初始:f[0][b] = 0,f[0][j] = 1
转移:f[i][j] = sum{f[i-1][p]|其中p∈[max(1,j-d+1),min(n,j+d-1)]且p!=j,其中d=abs(b-j)},即j位置可以从p位置花费一步转移来。
    - 用前缀和来优化这个转移，这样转移就是O(1)的，总体复杂度O(nk)。
答案:f[k][a]。
由于f[i]只需要f[i-1]计算，实现时用滚动数组。
注意卡BIT已试。
"""


#    TLE   ms
def solve1():
    n, a, b, k = RI()
    p = [1] * (n + 1)
    p[b] = 0
    f = BinIndexTree(p)
    # print(f)
    for _ in range(k):
        g = BinIndexTree(n + 1)
        for j in range(1, n + 1):
            if j == b:
                continue
            d = abs(b - j)
            l, r = max(1, j - d + 1), min(n, j + d - 1)
            g.add_point(j, f.sum_interval(l, j - 1) % MOD + f.sum_interval(j + 1, r))
        f = g
        # print(f)
    print(f.sum_interval(a, a) % MOD)


#   1045    ms
def solve2():
    n, a, b, k = RI()
    f = [1] * (n + 1)
    f[b] = 0
    for _ in range(k):
        g = [0] * (n + 1)
        p = [0] + list(accumulate(f))
        for j in range(1, n + 1):
            if j == b:
                continue
            d = abs(b - j)
            l, r = max(1, j - d + 1), min(n, j + d - 1)
            # g[j] = (p[j] - p[l] + p[r + 1] - p[j + 1]) % MOD
            g[j] = (p[r + 1] - p[l] - f[j]) % MOD
        f = g
    print(f[a])


#   733    ms
def solve():
    n, a, b, k = RI()
    f = [1] * (n + 1)
    f[b] = 0
    for _ in range(k):
        p = [0] + list(accumulate(f))
        for j in range(1, n + 1):
            if j == b:
                continue
            d = abs(b - j)
            l, r = max(1, j - d + 1), min(n, j + d - 1)
            f[j] = (p[j] - p[l] + p[r + 1] - p[j + 1]) % MOD

    print(f[a])


# 639ms
if __name__ == '__main__':
    n, a, b, k = RI()
    f = [1] * (n + 1)
    for _ in range(k):
        p = [0] + list(accumulate(f))
        for j in range(1, n + 1):
            d = b - j if b >= j else j - b
            l, r = j - d + 1 if j - d + 1 > 1 else 1, j + d - 1 if j + d - 1 < n else n
            f[j] = (p[j] - p[l] + p[r + 1] - p[j + 1]) % MOD

    print(f[a])
