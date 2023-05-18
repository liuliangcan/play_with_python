# Problem: G. Restore the Permutation
# Contest: Codeforces - Codeforces Round  834 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1759/G
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1759/G

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入偶数 n(2≤n≤2e5) 和长为 n/2 的数组 b(1≤b[i]≤n)，下标从 1 开始。

构造一个长为 n 的 1~n 的排列 p（下标从 1 开始），满足 max(p[2*i-1],p[2*i]) = b[i]。
如果无法构造，输出 -1，否则输出字典序最小的 p。
输入
6
6
4 3 6
4
2 4
8
8 7 2 3
6
6 4 2
4
4 4
8
8 7 4 5
输出
1 4 2 3 5 6
1 2 3 4
-1
5 6 3 4 1 2
-1
1 8 6 7 2 4 3 5
"""
"""https://codeforces.com/problemset/submission/1759/206226901

正难则反。

从大往小填数字。

例如最后一个样例，先填 6，必须和 8 或者 7 在一起，越靠后越好。
这意味着我们需要用一个最大堆去维护 b[i] 的下标，每次取堆顶下标减一的位置填数。
灵神这个题解有点看不懂 是按要填的数字视角遍历的吗
堆里访问过的数字都比当前数字大，所以跟谁配对都可以，选下标最大的配对这样？
"""
"""贪心+并查集
- 题目实际要求答案排列：每两个一组，分n/2组；从头数每组取max=b[i]。那这俩数里必有一个b[i]有一个小于b[i]的数x。
    - 由于要字典序最小，我们选择把x放b[i]前边。则p[1::2]=b，即把b[i]填到每组的第二个位置上。
- 从上边的讨论同时可以看出，如果b中有1，那无法构造答案(1和谁一组都不能是1)；如果没有n，也无法构造。(n和谁一组都是n)；
    - case很良心的，发现b中有重复数据也无法构造。
- 每个数只能分配比它小的数，为了使字典序最小，那么给靠前的数直接分配最小的数1吗。这可能导致给前边的n分配了1，后边的2无法分配。
    - 尽可能完成构造的贪心策略：对于数字b[i]分配一个比它小的最大数。若没有比它小的数则返回-1.
- 由于我们优先分配大数，因此倒序处理。
---
- 为了寻找小于b的最大数，用并查集，用掉一个数字v就连接(v,v-1)。这样比v小的最大数就是find_fa(v)。（左边最靠近v的数字）
"""


class DSU:
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.setCount = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        # if self.size[x] > self.size[y]:  # 注意如果要定向合并x->y，需要干掉这个；实际上上边改成find_fa后，按轶合并没必要了，所以可以常关
        #     x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.setCount -= 1
        return True


#   265    ms
def solve1():
    n, = RI()
    b = RILST()
    s = set(b)
    if len(s) * 2 != n:  # 是排列，有相同数字肯定不行
        return print(-1)
    if 1 in s or n not in s:  # 没有n或者有1都不行
        return print(-1)

    dsu = DSU(n + 1)
    for v in b:  # 用掉b里的数字
        dsu.union(v, v - 1)
    p = [0] * n
    p[1::2] = b
    for i in range(n - 2, -1, -2):
        v = dsu.find_fa(p[i + 1])
        if v == 0:
            return print(-1)
        dsu.union(v, v - 1)
        p[i] = v
    print(*p)


#     187  ms
def solve2():
    n, = RI()
    b = RILST()
    fs = list(range(n + 1))

    def find_fa(x):
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    cnt = n
    for v in b:  # 用掉b里的数字
        x, y = find_fa(v), find_fa(v - 1)
        if x != y:
            cnt -= 1
        else:  # 相同说明这个数用过了，b里有重复数据
            return print(-1)
        fs[x] = fs[y]
    p = [0] * n
    p[1::2] = b
    for i in range(n - 2, -1, -2):
        v = find_fa(p[i + 1])
        if v == 0:
            return print(-1)
        fs[v] = fs[find_fa(v - 1)]
        cnt -= 1
        p[i] = v
    if cnt:
        return print(-1)
    print(*p)


#     155  ms
def solve():
    n, = RI()
    b = RILST()
    fs = list(range(n + 1))

    def find_fa(x):
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    cnt = n
    for v in b:  # 用掉b里的数字
        x, y = find_fa(v), find_fa(v - 1)
        if x != y:
            cnt -= 1
        else:  # 相同说明这个数用过了，b里有重复数据
            return print(-1)
        fs[x] = fs[y]
    p = [0] * n
    p[1::2] = b
    for i in range(n - 2, -1, -2):
        v = find_fa(p[i + 1])
        if v == 0:
            return print(-1)
        fs[v] = fs[find_fa(v - 1)]
        cnt -= 1
        p[i] = v
    if cnt:
        return print(-1)
    print(' '.join(map(str, p)))


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
