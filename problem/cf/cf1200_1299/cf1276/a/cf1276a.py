# Problem: A. As Simple as One and Two
# Contest: Codeforces - Codeforces Round 606 (Div. 1, based on Technocup 2020 Elimination Round 4)
# URL: https://codeforces.com/problemset/problem/1276/A
# Memory Limit: 256 MB
# Time Limit: 3000 ms

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
PROBLEM = """https://codeforces.com/problemset/problem/1276/A

输入 T(≤1e4) 表示 T 组数据。所有数据字符串长度之和 ≤1.5e6。
每组数据输入一个长度 ≤1.5e5 的字符串 s，只包含小写字母。
删除尽量少的字符，使得字符串中不存在任何连续子串为 one 或 two。
输出：第一行为删除的字符个数。第二行为删除的字符下标（下标从 1 开始）。
输入
4
onetwone
testme
oneoneone
twotwo
输出
2
6 3
0

3
4 1 7
2
1 4
"""
"""注意到对于 oooneee 这样的字符串，删除 o 或 e 仍然会产生 one，但是删除 n 就不会有 one 了。
同理对于 two 应该删除 w。但是，如果子串是 twone，删除 o 更好。

https://codeforces.com/problemset/submission/1276/216058616"""


#  171     ms
def solve():
    s, = RS()
    n = len(s)
    p = {'one', 'two'}
    ans = []
    i = 0
    while i < n:
        if s[i:i + 5] == 'twone':
            ans.append(i + 3)
            i += 4
        elif s[i:i + 3] in p:
            ans.append(i + 2)
            i += 2
        i += 1
    print(len(ans))
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
