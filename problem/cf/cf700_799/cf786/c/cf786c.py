# Problem: C. Till I Collapse
# Contest: Codeforces - Codeforces Round 406 (Div. 1)
# URL: https://codeforces.com/contest/786/problem/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from collections import deque
from math import log2
from types import GeneratorType

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RILST = lambda: list(RI())
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/786/problem/C

输入 n(1≤n≤1e5) 和长为 n 的数组 a(1≤a[i]≤n)。

定义 f(k) 为最小的 m，使得存在一种将 a 划分成 m 段的方式，其中每段的不同数字个数都不超过 k。
输出 f(1), f(2), ... ,f(n)。
输入
5
1 3 4 3 3
输出
4 2 1 1 1

输入
8
1 5 7 8 1 7 6 1
输出
8 4 3 2 1 1 1 1
"""
"""https://codeforces.com/contest/786/submission/203881564

如果所有 a[i] 都不同，那么 f(k) 的图像与 ceil(n/k) 一样，k 越大，f(k) 越小，且存在若干段连续的 k，每一段的 f(k) 都相同。进而想到，如果有相同的 a[i]，那么图像也应当是类似的。

根据这一性质，可以不去计算所有的 f(k)，而是暴力计算两个 f(i) 和 f(j)，如果 f(i) = f(j)，那么从 i+1,i+2,...,j-1 的 f 值都等于 f(i)。
如何选取 i 和 j 呢？
分治 [1,n]，让程序自动帮你选。
如果 f(i) != f(j) 就取 mid = (i+j)/2 继续分治。

计算 f(k) 直接暴力遍历+贪心，如果当前不同元素个数超过 k，就开一个新的段，重新统计。
代码实现时可以用时间戳标记，避免反复创建 vis 数组/哈希表。

时间复杂度 O(n√n)。"""
"""py时间卡的挺死的。做如下优化：
放弃封装进solve，写到main里
f(i)使用灵神的时间戳技巧。
dfs改while ,至此可以ac
暴力处理前sqrt(n)或log2n个答案：这是因为这些答案更不容易重复
---
这些优化最重要的是第一条。
说明在函数内部(非全局)的func call是很占时间的。
"""


class FastIO:
    def __init__(self):
        return

    @staticmethod
    def _read():
        return sys.stdin.readline().strip()

    def read_int(self):
        return int(self._read())

    def read_float(self):
        return float(self._read())

    def read_ints(self):
        return map(int, self._read().split())

    def read_floats(self):
        return map(float, self._read().split())

    def read_ints_minus_one(self):
        return map(lambda x: int(x) - 1, self._read().split())

    def read_list_ints(self):
        return list(map(int, self._read().split()))

    def read_list_floats(self):
        return list(map(float, self._read().split()))

    def read_list_ints_minus_one(self):
        return list(map(lambda x: int(x) - 1, self._read().split()))

    def read_str(self):
        return self._read()

    def read_list_strs(self):
        return self._read().split()

    def read_list_str(self):
        return list(self._read())

    @staticmethod
    def st(x):
        return sys.stdout.write(str(x) + '\n')

    @staticmethod
    def lst(x):
        return print(*x)

    @staticmethod
    def round_5(f):
        res = int(f)
        if f - res >= 0.5:
            res += 1
        return res

    @staticmethod
    def max(a, b):
        return a if a > b else b

    @staticmethod
    def min(a, b):
        return a if a < b else b

    @staticmethod
    def bootstrap(f, queue=[]):
        def wrappedfunc(*args, **kwargs):
            if queue:
                return f(*args, **kwargs)
            else:
                to = f(*args, **kwargs)
                while True:
                    if isinstance(to, GeneratorType):
                        queue.append(to)
                        to = next(to)
                    else:
                        queue.pop()
                        if not queue:
                            break
                        to = queue[-1].send(to)
                return to

        return wrappedfunc

    def ask(self, lst):
        self.lst(lst)
        sys.stdout.flush()
        res = self.read_int()
        return res

    @staticmethod
    def accumulate(nums):
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        return pre


#  TLE8
def solve1():
    n, = RI()
    a = RILST()
    ans = [0] * (n + 1)

    def f(k):
        m = 1
        s = set()
        for v in a:
            s.add(v)
            if len(s) > k:
                s = {v}
                m += 1
        return m

    def dfs(l, r):
        if not ans[l]: ans[l] = f(l)
        if not ans[r]: ans[r] = f(r)

        if l + 1 >= r:
            return

        if ans[l] == ans[r]:
            for i in range(l + 1, r):
                ans[i] = ans[l]
            return
        mid = (l + r) // 2
        dfs(l, mid)
        dfs(mid, r)

    dfs(1, n)
    print(*ans[1:])


#     TLE8
def solve3():
    n, = RI()
    a = RILST()
    ans = [0] * (n + 1)
    time = [0] * (n + 1)
    clock = 1

    def f(k):
        nonlocal clock
        clock += 1
        m = 1
        cnt = 0

        for v in a:
            if time[v] == clock:
                continue
            cnt += 1
            if cnt > k:
                m += 1
                clock += 1
                cnt = 1
            time[v] = clock
        return m

    def dfs(l, r):
        if not ans[l]: ans[l] = f(l)
        if not ans[r]: ans[r] = f(r)

        if l + 1 >= r:
            return

        if ans[l] == ans[r]:
            for i in range(l + 1, r):
                ans[i] = ans[l]
            return
        mid = (l + r) // 2
        dfs(l + 1, mid)
        dfs(mid + 1, r - 1)

    dfs(1, n)
    print(*ans[1:])


#   tle8    ms
def solve2():
    n, = RI()
    a = RILST()
    ans = [0] * (n + 1)
    time = [0] * (n + 1)
    clock = 1

    def f(k):
        nonlocal clock
        clock += 1
        m = 1
        cnt = 0

        for v in a:
            if time[v] == clock:
                continue
            cnt += 1
            if cnt > k:
                m += 1
                clock += 1
                cnt = 1
            time[v] = clock
        return m

    def dfs(l, r):
        if not ans[l]: ans[l] = f(l)
        if not ans[r]: ans[r] = f(r)

        if l + 1 >= r:
            return

        if ans[l] == ans[r]:
            for i in range(l + 1, r):
                ans[i] = ans[l]
            return
        mid = (l + r) // 2
        dfs(l, mid)
        dfs(mid, r)

    dfs(1, n)
    # print(*ans[1:])
    print(' '.join(map(str, ans[1:])))


clock = 1


#   tle8    ms
def solve():
    n, = RI()
    a = RILST()
    ans = [0] * (n + 1)
    time = [0] * (n + 1)

    # clock = 1

    def f(k):
        global clock
        clock += 1
        m = 1
        cnt = 0

        for v in a:
            if time[v] == clock:
                continue
            cnt += 1
            if cnt > k:
                m += 1
                clock += 1
                cnt = 1
            time[v] = clock
        return m

    L = min(2 * int(n ** 0.5), n - 1)
    for i in range(1, L + 1):
        ans[i] = f(i)
    q = [(L, n)]
    while q:
        nq = []
        for l, r in q:
            if not ans[l]: ans[l] = f(l)
            if not ans[r]: ans[r] = f(r)

            if l + 1 >= r:
                continue
            if ans[l] == ans[r]:
                for i in range(l + 1, r):
                    ans[i] = ans[l]
                continue
            mid = (l + r) >> 1
            nq.append((l, mid))
            nq.append((mid, r))
        q = nq

    # print(*ans[1:])
    print(' '.join(map(str, ans[1:])))


# solve()
# if __name__ == '__main__':
#
#     solve()

def solve():
    n, = RI()
    a = RILST()
    ans = [0] * (n + 1)
    time = [0] * (n + 1)
    clock = 1

    # def f(k):
    #     global clock
    #     clock += 1
    #     m = 1
    #     cnt = 0
    #
    #     for v in a:
    #         if time[v] == clock:
    #             continue
    #         cnt += 1
    #         if cnt > k:
    #             m += 1
    #             clock += 1
    #             cnt = 1
    #         time[v] = clock
    #     return m

    L = min(int(log2(n)), n - 1)  # 936ms
    for i in range(1, L + 1):
        clock += 1
        m = 1
        cnt = 0

        for v in a:
            if time[v] == clock:
                continue
            cnt += 1
            if cnt > i:
                m += 1
                clock += 1
                cnt = 1
            time[v] = clock

        ans[i] = m

    q = [(L, n)]
    while q:
        nq = []
        for l, r in q:
            if not ans[l]:
                clock += 1
                m = 1
                cnt = 0

                for v in a:
                    if time[v] == clock:
                        continue
                    cnt += 1
                    if cnt > l:
                        m += 1
                        clock += 1
                        cnt = 1
                    time[v] = clock

                ans[l] = m
            if not ans[r]:
                clock += 1
                m = 1
                cnt = 0

                for v in a:
                    if time[v] == clock:
                        continue
                    cnt += 1
                    if cnt > r:
                        m += 1
                        clock += 1
                        cnt = 1
                    time[v] = clock
                ans[r] = m

            if l + 1 >= r:
                continue
            if ans[l] == ans[r]:
                for i in range(l + 1, r):
                    ans[i] = ans[l]
                continue
            mid = (l + r) >> 1
            nq.append((l, mid))
            nq.append((mid, r))
        q = nq

    # print(*ans[1:])
    print(' '.join(map(str, ans[1:])))


if __name__ == '__main__':
    # solve()
    n, = RI()
    a = RILST()
    ans = [0] * (n + 1)
    time = [0] * (n + 1)
    clock = 1


    def f(k):
        global clock
        clock += 1
        m = 1
        cnt = 0

        for v in a:
            if time[v] == clock:
                continue
            cnt += 1
            if cnt > k:
                m += 1
                clock += 1
                cnt = 1
            time[v] = clock
        return m


    L = min(int(log2(n)), n - 1)  # 936ms
    for i in range(1, L + 1):
        ans[i] = f(i)

    q = [(L, n)]
    while q:
        nq = []
        for l, r in q:
            if not ans[l]: ans[l] = f(l)
            if not ans[r]: ans[r] = f(r)

            if l + 1 >= r:
                continue
            if ans[l] == ans[r]:
                for i in range(l + 1, r):
                    ans[i] = ans[l]
                continue
            mid = (l + r) >> 1
            nq.append((l, mid))
            nq.append((mid, r))
        q = nq

    # print(*ans[1:])
    print(' '.join(map(str, ans[1:])))
