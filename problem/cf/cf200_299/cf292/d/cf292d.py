# Problem: D. Connected Components
# Contest: Codeforces - Croc Champ 2013 - Round 1
# URL: https://codeforces.com/problemset/problem/292/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/292/D

输入 n(2≤n≤500) m(1≤m≤1e4) 和一个无向图的 m 条边，节点编号从 1 到 n，无自环，可能有重边。
然后输入 k(1≤k≤2e4) 个询问，每个询问输入 left 和 right，表示删除第 left 到第 right 条边（边按照输入编号，从 1 到 m）。
对每个询问，输出删除边后，此时有多少个连通块。
请注意：每个询问都是独立的，在下个询问前会恢复成原图。
输入
6 5
1 2
5 4
2 3
3 1
3 6
6
1 3
2 5
1 5
5 5
2 4
3 3
输出
4
5
6
3
4
2
"""
"""https://codeforces.com/contest/292/submission/173783235

前后缀分解。

预处理，对 m 条边的每个前缀和每个后缀建立大小为 n 的并查集，递推计算。每次递推在上一个并查集的基础上计算，预处理总时间 O(nm)。（每次递推都要 copy 一次并查集）
对每个询问，把对应的前缀与后缀的并查集合并（对每个 i，把前缀的 fa[i] 与后缀的 fa[i] 合并），这样每个询问只需要 O(n) 的时间。（暴力是 O(m)）"""


#   1808    ms
def solve():
    n, m = RI()
    es = []
    pre = [list(range(n))]
    ps = [n]
    for _ in range(m):
        u, v = RI()
        u -= 1
        v -= 1
        es.append((u, v))
        fa = pre[-1][:]
        pre.append(fa)
        ps.append(ps[-1])
        u, v = find(fa, u), find(fa, v)
        if u != v:
            ps[-1] -= 1
            fa[u] = v
    suf = [list(range(n))]
    ss = [n]

    for u, v in es[::-1]:
        fa = suf[-1][:]
        suf.append(fa)
        ss.append(ss[-1])
        u, v = find(fa, u), find(fa, v)
        if u != v:
            fa[u] = v
            ss[-1] -= 1
    suf = suf[::-1]
    ss = ss[::-1]

    k, = RI()
    for _ in range(k):
        l, r = RI()
        if r == m:
            print(ps[l - 1])
            continue
        if l == 1:
            print(ss[r])
            continue

        fa = pre[l - 1][:]
        ans = ps[l - 1]

        for i, (u, v) in enumerate(zip(fa, suf[r])):
            if v == i: continue
            u, v = find(fa, u), find(fa, v)
            if u != v:
                ans -= 1
                fa[u] = v

        print(ans)


def find(fa, x):
    t = x
    while fa[x] != x:
        x = fa[x]
    while t != x:
        fa[t], t = x, fa[t]
    return x


# 1808
if __name__ == '__main__':
    n, m = RI()
    es = []
    b = 20  # 按b分块，不存那么多并查集,实测效果不好，还是应该搞
    fa = list(range(n))
    size = n
    pre = [fa[:]]
    ps = [n]
    for i in range(1, m + 1):
        u, v = RI()
        u -= 1
        v -= 1
        es.append((u, v))

        u, v = find(fa, u), find(fa, v)
        if u != v:
            size -= 1
            fa[u] = v
        if i % b == 0:
            pre.append(fa[:])
            ps.append(size)

    fa = list(range(n))
    suf = [fa[:]]

    for i in range(m, 0, -1):
        u, v = es[i - 1]
        u, v = find(fa, u), find(fa, v)
        if u != v:
            fa[u] = v
        if i % b == 0:
            suf.append(fa[:])

    suf = suf[::-1]

    k, = RI()
    for _ in range(k):
        l, r = RI()
        p = (l - 1) // b
        fa = pre[p][:]
        ans = ps[p]

        # if n == 500 and m == 1000:
        #     print(l, r, ans, p, len(suf))
        # print(0,ans,p,l)
        for i in range(p * b + 1, l):
            u, v = es[i - 1]
            u, v = find(fa, u), find(fa, v)
            if u != v:
                ans -= 1
                fa[u] = v
        # print(1,ans)

        # if n == 500 and m == 1000:
        #     print(l, r, ans, p * b)
        p = r // b + 1

        for i, (u, v) in enumerate(zip(fa, suf[p - 1])):
            if v == i: continue
            u, v = find(fa, u), find(fa, v)
            if u != v:
                ans -= 1
                fa[u] = v

        # if n == 500 and m == 1000:
        #     print(l, r, ans, p, len(set(suf[p - 1])))
        for i in range(r + 1, min(p * b, m + 1)):
            u, v = es[i - 1]
            u, v = find(fa, u), find(fa, v)
            if u != v:
                ans -= 1
                fa[u] = v

        # if n == 500 and m == 1000:
        #     print(l, r, ans, p * b)
        print(ans)
