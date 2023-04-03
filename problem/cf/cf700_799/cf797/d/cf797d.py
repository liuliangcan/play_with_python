# Problem: D. Broken BST
# Contest: Codeforces - Educational Codeforces Round 19
# URL: https://codeforces.com/contest/797/problem/D
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/797/problem/D

输入 n(1≤n≤1e5) 和一棵二叉树的 n 个节点，每行输入 x l r，对应节点值 [0,1e9] 和左右儿子的编号 [1,n]，如果没有则为 -1。
输入保证恰好有一个节点没有父节点，即根节点。

如下是一个在二叉搜索树中查找元素的伪代码：
bool find(TreeNode t, int x) {
    if (t == null)
        return false;
    if (t.value == x)
        return true;
    if (x < t.value)
        return find(t.left, x);
    else
        return find(t.right, x);
}
find(root, x);

把二叉树的每个节点值应用上述代码，输出你会得到多少次 false。
注意节点值可能有重复的。
输入
3
15 -1 -1
10 1 3
5 -1 -1
输出 2
解释 5 和 15 是找不到的
"""
"""https://codeforces.com/contest/797/submission/190439455

考虑有多少个节点值可以找到。
参考 https://www.bilibili.com/video/BV14G411P7C1/ 的方法一，把合法查询范围作为递归参数传下去。
如果节点值 x 在范围内，则有 cnt[x] 个 x 可以找到。

注：用 cnt 是因为有重复的节点，这些节点值都可以找到（即使某些节点无法访问到）。
"""


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


#       ms
def solve():
    n, = RI()
    a = []
    has_fa = [False] * n
    cnt = Counter()
    for i in range(n):
        v, l, r = RI()
        l -= 1
        r -= 1
        cnt[v] += 1
        a.append((v, l, r))
        if l >= 0:
            has_fa[l] = True
        if r >= 0:
            has_fa[r] = True
    root = 0
    while has_fa[root]:
        root += 1
    ans = n
    q = deque([(root, 0, 10 ** 9)])
    while q:
        # i, l, r = q.popleft()  # 358ms
        i, l, r = q.pop()  # 249ms
        v, x, y = a[i]
        if l <= v <= r:
            ans -= cnt[v]
        if l < v and x >= 0:
            q.append((x, l, min(r, v - 1)))
        if r > v and y >= 0:
            q.append((y, max(l, v + 1), r))
    print(ans)


if __name__ == '__main__':
    solve()
