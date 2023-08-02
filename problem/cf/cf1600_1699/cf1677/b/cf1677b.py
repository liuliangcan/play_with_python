# Problem: B. Tokitsukaze and Meeting
# Contest: Codeforces - Codeforces Round 789 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1677/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1677/B

输入 T(≤1e4) 表示 T 组数据。所有数据的 n*m 之和 ≤1e6。
每组数据输入 n m(1≤n*m≤1e6) 和长为 n*m 的 01 字符串 s。

有 n*m 个人参加会议，会议厅的座位有 n 行 m 列。
从第一个人开始，依次入场。规则如下：
有人入场时，已入场的人同时向右移动一位，最右的人移动到下一行的最左边。（见样例一）
第 i 个人标记为 s[i]。
输出 n*m 个数，其中第 i 个数表示：第 i 个人入场后，有多少行和列包含至少一个 1？
输入
3
2 2
1100
4 2
11001101
2 4
11001101
输出
2 3 4 3
2 3 4 3 5 4 6 5
2 3 3 3 4 4 4 5

样例一见右图
"""
"""好题！迷你，精巧，还同时考察了多个知识点。

先说列怎么统计：

提示 1：从「不变量」入手思考：第 i 个人总是和第 i-m,i-2m,i-3m,... 个人在同一列。

提示 2：如果 i-m,i-2m,i-3m,... 中没有 1，那么当 s[i]=1 入场，从这一刻开始，包含至少一个 1 的列的数量永久增加 1。

然后说行怎么统计：

提示 1：考虑第 i 个人入场时，包含至少一个 1 的行的数量。这等于「第 i-m 个人入场时，包含至少一个 1 的行的数量」加上「最新入场的这 m 个人中是否有 1」。

提示 2：滑动窗口维护「最新入场的这 m 个人中的 1 的个数」，记作 window1。
DP 维护「第 i 个人入场时，包含至少一个 1 的行的数量」，即
f[i] = f[i-m] + (window1 > 0)
这个转移方程可以滚动优化成 f[i%m] += window1 > 0，从而避免讨论 i<m 的情况（此时 i-m 是负数）。

https://codeforces.com/contest/1677/submission/216653925"""

#       ms
def solve1():
    n, m = RI()
    s, = RS()
    col = [0] * m
    cnt_col = 0
    ans = []
    f = [0] * m
    q = deque()
    w = 0
    for i, c in enumerate(s):
        q.append(c)
        if c == '1':
            w += 1
            if not col[i % m]:
                col[i % m] = 1
                cnt_col += 1
        if len(q) > m:
            w -= q.popleft() == '1'
        f[i % m] += w > 0
        ans.append(f[i % m] + cnt_col)
    print(' '.join(map(str, ans)))


#       ms
def solve():
    n, m = RI()
    s, = RS()
    col = [0] * m
    cnt_col = 0
    ans = []
    f = [0] * m
    w = 0
    l = 0
    for i, c in enumerate(s):
        if c == '1':
            w += 1
            if not col[i % m]:
                col[i % m] = 1
                cnt_col += 1
        if i - l + 1 > m:
            w -= s[l] == '1'
            l += 1
        f[i % m] += w > 0
        ans.append(f[i % m] + cnt_col)
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
