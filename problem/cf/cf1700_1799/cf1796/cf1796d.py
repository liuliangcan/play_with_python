# Problem: D. Maximum Subarray
# Contest: Codeforces - Educational Codeforces Round 144 (Rated for Div. 2)
# URL: https://codeforces.com/contest/1796/problem/D
# Memory Limit: 512 MB
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

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
"""https://codeforces.com/problemset/problem/1796/D

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(1≤n≤2e5) k(0≤k≤min(20,n)) x(-1e9≤x≤1e9) 和长为 n 的数组 a(-1e9≤a[i]≤1e9)。

你需要把 a 中恰好 k 个数增加 x，其余数减少 x。
该操作必须恰好执行一次。
在最优操作下，a 的最大连续子数组和的最大值是多少？
注意子数组可以是空的，元素和为 0。

进阶：你能做到 O(n) 吗？复杂度和 k 无关。
输入
4
4 1 2
2 -1 2 3
2 2 3
-1 2
3 0 5
3 2 4
6 2 -8
4 -1 9 -3 7 -8
输出
5
7
0
44
"""
"""O(n) 做法如下。

如果 x<0，那么可以把 x 变成 -x，同时 k 变成 n-k。
下面的讨论满足 x>=0。

为方便计算，先把所有数都减去 x，于是操作变成把 k 个数增加 2x。

分类讨论：
1. 如果子数组长度超过 k，那么子数组内有 k 个数可以增加 2x，总和增加 2kx。我们计算的是长度有下限的最大子数组和。
用前缀和思考，s[right]-s[left] 最大，那么 s[left] 尽量小，且 right-left > k，所以枚举 right 的同时，要维护 s[0] 到 s[right-k-1] 的最小值。
如果你不知道这个做法，可以先看【题解】最大子数组和的前缀和做法
2. 如果子数组长度不超过 k，那么子数组内所有数都可以增加 2x。我们计算的是长度有上限的最大子数组和，这可以用前缀和+单调队列解决。做法类似滑动窗口最大值，如果你不知道这个做法，可以看 【视频】滑动窗口最大值

总的来说，这题同时考察了最大子数组和的长度下限变体和长度上限变体，是一道不错的综合题目。

代码"""


def kadane(a):
    ans, s = a[0], 0
    for v in a:
        s = max(0, s) + v
        ans = max(ans, s)
    return ans


"""
func cf1796D(in io.Reader, out io.Writer) {
	var T, n, k, x int
	for Fscan(in, &T); T > 0; T-- {
		Fscan(in, &n, &k, &x)
		if x < 0 {
			x = -x
			k = n - k
		}
 
		var ans, pre, pre2, minS int
		a := make([]int, n)
		for i := range a {
			Fscan(in, &a[i])
			pre += a[i] - x
			if i >= k {
				ans = max(ans, pre-minS+k*x*2)
				pre2 += a[i-k] - x
				minS = min(minS, pre2)
			}
		}
 
 
		Fprintln(out, ans)
	}
}
"""


def get_max_sub_array_under_k(a, k):
    """长度<=k的最大子段和，不含空"""
    if k == 0:  # 长度不超过0那只好是空，看情况非法值修改成0或其他
        return -inf
    ans = -inf
    pre = [0] + list(accumulate(a))
    q = deque([0])  # 单调递增队列
    for i, v in enumerate(pre):
        while q[0] + k < i:
            q.popleft()  # k以外，出窗

        ans = max(ans, v - pre[q[0]])
        while q and pre[q[-1]] >= pre[i]:
            q.pop()  # 留小的
        q.append(i)
    return ans


def get_max_sub_array_over_k(a, k):
    """长度>=k的最大子段和,双指针+前缀和;注意k=0的情况，那就是没限制"""
    if k == 0:return kadane(a)

    ans = -inf
    pre = pre2 = mn = 0

    for i, v in enumerate(a):
        pre += v
        if i >= k - 1:
            ans = max(ans, pre - mn)
            pre2 += a[i - k + 1]
            mn = min(mn, pre2)

    return ans


def solve1():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    if x < 0:
        x = -x
        k = n - k
    ans = mn = s = sk = 0
    for i, v in enumerate(a):
        s += v - x
        if i >= k:
            ans = max(ans, s - mn + k * x * 2)
            sk += a[i - k] - x
            mn = min(mn, sk)
    pre = [0] + list(accumulate([v + x for v in a]))
    q = deque()
    for i, v in enumerate(pre):
        while q and q[0] < i - k:
            q.popleft()
        while q and pre[q[-1]] >= pre[i]:
            q.pop()
        q.append(i)
        ans = max(ans, pre[i] - pre[q[0]])
    print(ans)


#       ms
def solve():
    n, k, x = RI()
    a = RILST()
    if x < 0:
        x = -x
        k = n - k
    ans = max(0, get_max_sub_array_over_k([v - x for v in a], k) + k * 2 * x)
    ans = max(ans, get_max_sub_array_under_k([v + x for v in a], k))
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
