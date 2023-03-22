# Problem: C. Choosing flowers
# Contest: Codeforces - Codeforces Round 657 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1379/C
# Memory Limit: 512 MB
# Time Limit: 1000 ms

import sys
from bisect import *
from itertools import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1379/C

输入 t(≤1e4) 表示 t 组数据。所有数据的 m 之和 ≤1e5。

每组数据输入 n(≤1e9) m(≤1e5) 表示有 m 种物品，每种物品有无限个，你需要选择 n 个。
然后输入 m 行，每行两个数字 a[i] 和 b[i]，范围在 [0,1e9]。

如果第 i 种物品选 x 个（x>0），收益为 a[i]+(x-1)*b[i]。
输出最大收益。
输入
2
4 3
5 0
1 4
2 2

5 3
5 2
4 2
3 1
输出
14
16
"""
"""https://codeforces.com/contest/1379/submission/87405052

提示 1：至多有一个物品要选超过 1 个。（反证法：如果有两个，只选 b 更大的那个更优）

提示 2：枚举第 i 个物品选了超过 1 个，那么比 b[i] 大的物品必须选 1 个。

提示 3：对 a 排序，然后二分或者双指针。"""


#  389     ms
def solve1():
    n, m = RI()
    a = []
    ba = []
    ans = 0
    for _ in range(m):
        x, y = RI()
        a.append(x)
        ba.append((y, x))
    a.sort()
    ba.sort()
    i = m - 1
    s = 0
    for y, x in ba[::-1]:
        while n > 0 and i >= 0 and a[i] >= y:
            s += a[i]
            i -= 1
            n -= 1
        if n <= 0:
            ans = max(ans, s)
            break
        if x >= y:
            ans = max(ans, s + n * y)
        else:
            ans = max(ans, s + x + (n - 1) * y)

    print(ans)


#    171   ms
def solve():
    n, m = RI()
    a = []
    ba = []
    ans = 0
    for _ in range(m):
        x, y = RI()
        a.append(x)
        # ans = max(ans, x + y * (n - 1))
        ba.append((y, x))
    a.sort()
    pa = [0] + list(accumulate(a))
    if n <= m:  # 如果n很小，直接尝试取最大的n个a，即各取1个的方案。
        ans = pa[-1] - pa[m - n]
    for y, x in ba:
        p = bisect_left(a, y)
        z = m - p
        if z >= n:  # 由于这z个物品必须至少选1个，那超过n就不用考虑了
            # ans = max(ans, pa[-1] - pa[m - n])
            continue
        if x >= y:
            ans = max(ans, pa[-1] - pa[m - z] + (n - z) * y)
        else:
            ans = max(ans, pa[-1] - pa[m - z] + x + (n - z - 1) * y)
        # s = pa[-1] - pa[m - z] + (n - z) * y
        # if x < y:
        #     s += x - y
        # if s > ans:
        #     ans = s
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
        RS()
