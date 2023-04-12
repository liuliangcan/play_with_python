import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1296/C

输入 t(≤1e3) 表示 t 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(≤2e5) 和长为 n 的字符串 s，仅包含 LRUD，分别表示左右上下四个方向。

一个机器人初始在 (0,0)，按照 s 移动，每一步移动一个单位长度。
设机器人最终移动到了 (x,y)。
你需要从 s 中删除一段尽量短的非空连续子串，得到 s'，使得机器人从 (0,0) 出发，按照 s' 也能移动到 (x,y)。
输出你删除的这段子串的左右端点（下标从 1 开始）。
如果无法做到，输出 -1。
输入
4
4
LRUD
4
LURD
5
RRUDU
5
LLDDR
输出
1 2
1 4
3 4
-1
"""
"""前缀和哈希即可
我这里把xy组合了，其实不用，哈希tuple也可以。
"""
l, r, u, d = 10 ** 6, -10 ** 6, 1, -1


#    109   ms
def solve():
    n, = RI()
    s, = RS()
    p = 0
    idx = {0: 0}
    trans = {'L': 1, 'R': -1, 'U': 10 ** 6, 'D': -10 ** 6}
    ans = [1, n + 1]
    for i, c in enumerate(s, start=1):
        p += trans[c]
        if p in idx:
            l = idx[p] + 1
            if i - l < ans[-1] - ans[0]:
                ans = [l, i]
        idx[p] = i
    if ans == [1, n + 1]:
        return print(-1)
    print(*ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
