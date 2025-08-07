# Problem: G. (Zero XOR Subset)-less
# Contest: Codeforces - Educational Codeforces Round 58 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1101/G
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from functools import reduce
from operator import xor

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RILST = lambda: list(RI())

# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1101/G

输入 n(1≤n≤2e5) 和长为 n 的数组 a(0≤a[i]≤1e9)。

把 a 分割成若干段（连续非空子数组），要求：从这些子段中任取若干子段，它们包含的所有数的异或和不能为 0。

输出最多能分成多少段。
如果不存在合法分割方案，输出 -1。
输入
4
5 5 7 2
输出 2

输入
3
1 2 3
输出 -1

输入
3
3 1 10
输出 3
"""
"""首先判断 -1。
如果整个数组的异或和等于 0，那么无论怎么分割，只要全选，异或和就是 0。无解。
否则一定有解（比如不分割）。

用前缀异或和思考。
比如 $a=[1,2]$，前缀异或和数组为 $s=[0,1,3]$。可以用 1 和 3 当作基。
选择的子段为 [1]，异或和为 1，即 s[0]^s[1] = 1。
选择的子段为 [1,2]，异或和为 3，即 s[0]^s[2] = 3。
选择的子段为 [2]，异或和为 1^3，即 s[1]^s[2] = 2。

一般地，问题相当于从前缀和数组（除去 s[0]=0）中选择一些数，这些数的任意非空子集的异或和不为 0。
解释：
如果选了偶数个数，可以两两一对，每一对对应一段。
如果选了奇数个数，那么把 s[0]=0 也选上，变成选偶数个数的情况。
反之，如果存在一个子集的异或和等于 0，可以按照上述奇偶分类讨论，能够对应到一种不合法的分割方案。

所以当且仅当从前缀和数组（除去 s[0]=0）中选择一些数，这些数的任意非空子集的异或和不为 0 时，分割方案是合法的。
答案为线性基中的基的个数。每成功插入一个基，就把答案加一。
如果不仅选了基，还选了可以被基表出的数，那么这个数和对应的基一起，异或和为 0，对应着某些段的异或和为 0。

代码实现时，由于前缀异或和可以由原数组的基表出，所以可以直接计算原数组的线性基，无需计算前缀异或和的线性基。

代码
代码备份（Ubuntu Pastebin）
"""


#  高斯消元     ms
def solve():
    n, = RI()
    a = RILST()

    if reduce(xor, a) == 0:
        return print(-1)

    cnt = 0
    for i in range(max(a).bit_length() - 1, -1, -1):
        for j in range(cnt, n):
            if a[j] >> i & 1:
                a[cnt], a[j] = a[j], a[cnt]
                break
        else:continue
        for j in range(n):
            if j != cnt and a[j] >> i & 1:
                a[j] ^= a[cnt]
        cnt += 1
        # if cnt == n: break

    print(cnt)


#  奇怪法156     ms
def solve2():
    n, = RI()
    a = RILST()

    if reduce(xor, a) == 0:
        return print(-1)

    b = []
    for v in a:
        for x in b:
            v = min(v, v ^ x)
        if v:
            b.append(v)

    print(len(b))


#   贪心法171    ms
def solve1():
    n, = RI()
    a = RILST()

    if reduce(xor, a) == 0:
        return print(-1)
    mx = max(a)
    b = [0] * mx.bit_length()
    ans = 0
    for v in a:
        while v:
            i = v.bit_length() - 1
            if b[i] == 0:
                b[i] = v
                ans += 1
                break
            v ^= b[i]
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
