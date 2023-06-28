# Problem: C. Monsters And Spells
# Contest: Codeforces - Educational Codeforces Round 121 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1626/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1626/C

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤1e4。
每组数据输入 n(1≤n≤100) 和长为 n 的严格递增数组 k，长为 n 的数组 h (1≤h[i]≤k[i]≤1e9)。

你在玩一个打怪游戏。有 n 只怪物，第 i 只会在第 k[i] 秒出现，血量为 h[i]。
你有一个引导类法术，你引导的时间越长，伤害越高，消耗的魔法值也越高。
具体来说，开始引导的第 1 秒，伤害为 1，消耗 1；第 2 秒，伤害为 2，消耗 2；第 i 秒，伤害为 i，消耗 i。
例如，伤害达到 3，要消耗 1+2+3=6 的魔法值。
你可以随时停止引导（停止后伤害为 0），或者重新引导（从 1 开始）。

游戏从第 1 秒开始。在第 k[i] 秒，法术伤害至少要是 h[i]。
要击败所有怪物，消耗的魔法值之和至少是多少？
输入
3
1
6
4
2
4 5
2 2
3
5 7 9
2 1 2
输出
10
6
7
"""


#   186    ms
def solve1():
    n, = RI()
    ks = RILST()
    hs = RILST()
    a = []
    for k, h in zip(ks, hs):
        a.append((k - h + 1, k))
    a.sort()
    ans = []
    x, y = a[0]
    for l, r in a[1:]:
        if l > y:
            ans.append((x, y))
            x = l
        y = max(y, r)
    ans.append((x, y))
    # print(ans)
    print(sum((y - x + 1) * (y - x + 2) // 2 for x, y in ans))


#   140    ms
def solve2():
    n, = RI()
    ks = RILST()
    hs = RILST()
    a = []
    for k, h in zip(ks, hs):
        a.append((k - h + 1, k))

    ans = 0
    x, y = a[-1]
    for l, r in a[n - 2::-1]:
        if r >= x:
            x = min(l, x)
        else:
            ans += (y - x + 1) * (y - x + 2) // 2
            x, y = l, r

    ans += (y - x + 1) * (y - x + 2) // 2
    print(ans)


#   140    ms
def solve():
    n, = RI()
    ks = RILST()
    hs = RILST()
    ans = 0
    x, y = 10 ** 10, 10 ** 10 - 1
    for k, h in zip(ks[::-1], hs[::-1]):
        l, r = k - h + 1, k
        if r >= x:
            x = min(x, l)
        else:
            ans += (y - x + 1) * (y - x + 2) // 2
            x, y = l, r

    ans += (y - x + 1) * (y - x + 2) // 2
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
