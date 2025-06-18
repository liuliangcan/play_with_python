

import sys
from array import array
from bisect import bisect_left
RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。
import gc
gc.disable()

# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/2104/E

输入 n(1≤n≤1e6) k(1≤k≤26) 和长为 n 的字符串 s，只包含前 k 个小写英文字母。
然后输入 q(1≤q≤2e5) 和 q 个询问，每个询问输入一个字符串 t，只包含前 k 个小写英文字母。保证所有 t 的长度之和 ≤1e6。

在 t 的末尾添加若干字母（必须是前 k 个小写英文字母），使得 t 不是 s 的子序列。
输出最少添加多少个字母。
输入
7 3
abacaba
3
cc
bcb
b
输出
0
1
2

输入
5 1
aaaaa
6
a
aa
aaa
aaaa
aaaaa
aaaaaa
输出
5
4
3
2
1
0
"""

def solve5():  # 827ms
    n, k = RI()
    s, = RS()
    f = array('i', [n]  *(n*k + k))
    suf = array('i', [0]*(n+1))

    mask = 0
    cnt = 0
    target = (1 << k) - 1
    for i in range(n - 1, -1, -1):
        v = ord(s[i]) - ord('a')
        mask |= 1 << v
        if mask == target:
            mask = 0
            cnt += 1
        suf[i] = cnt
        p = i*k
        f[p:p+k] = f[p+k:p+k*2]
        f[p+v] = i
    q, = RI()
    for _ in range(q):
        t, = RS()
        i = -1
        for c in t:
            i = f[(i + 1)*k + ord(c)-ord('a')]
            if i == n:
                print(0)
                break
        else:
            print(suf[i + 1] + 1)

def solve():  # 328ms
    n, k = RI()
    s, = RS()
    f = [n] * (n*k + k)
    suf = [0] * (n + 1)
    mask = 0
    cnt = 0
    target = (1 << k) - 1
    for i in range(n - 1, -1, -1):
        v = ord(s[i]) - ord('a')
        mask |= 1 << v
        if mask == target:
            mask = 0
            cnt += 1
        suf[i] = cnt
        p = i*k
        f[p:p+k] = f[p+k:p+k*2]
        f[p+v] = i
    q, = RI()
    for _ in range(q):
        t, = RS()
        i = -1
        for c in t:
            i = f[(i + 1)*k + ord(c)-ord('a')]
            if i == n:
                print(0)
                break
        else:
            print(suf[i + 1] + 1)


#       ms
def solve3():  # 499
    n, k = RI()
    s, = RS()
    s = [ord(c) - ord('a') for c in s]
    f = [[n] for _ in range(k)]
    suf = [0] * (n + 1)
    mask = 0
    cnt = 0
    target = (1 << k) - 1
    for i in range(n - 1, -1, -1):
        mask |= 1 << s[i]
        if mask == target:
            mask = 0
            cnt += 1
        suf[i] = cnt
        f[s[i]].append(i)
    for a in f:
        a.reverse()
    q, = RI()
    for _ in range(q):
        t, = RS()
        i = -1
        for c in t:
            a = f[ord(c) - ord('a')]
            i = a[bisect_left(a, i + 1)]
            if i == n:
                print(0)
                break
        else:
            print(suf[i + 1] + 1)


def solve2():  # 656ms
    n, k = RI()
    s, = RS()
    s = [ord(c) - ord('a') for c in s]
    f = [[n] * (n + 1) for _ in range(k)]
    suf = [0] * (n + 1)
    mask = 0
    cnt = 0
    target = (1 << k) - 1
    for i in range(n - 1, -1, -1):
        mask |= 1 << s[i]
        if mask == target:
            mask = 0
            cnt += 1
        suf[i] = cnt
        for j in range(k):
            f[j][i] = f[j][i + 1]
        f[s[i]][i] = i
    q, = RI()
    for _ in range(q):
        t, = RS()
        i = -1
        for c in t:
            i = f[ord(c) - ord('a')][i + 1]
            if i == n:
                print(0)
                break
        else:
            print(suf[i + 1] + 1)


#       ms
def solve1():  # MLE
    n, k = RI()
    s, = RS()
    s = [ord(c) - ord('a') for c in s]
    f = [[n] * k for _ in range(n + 1)]
    suf = [0] * (n + 1)
    mask = 0
    cnt = 0
    target = (1 << k) - 1
    for i in range(n - 1, -1, -1):
        mask |= 1 << s[i]
        if mask == target:
            mask = 0
            cnt += 1
        suf[i] = cnt
        f[i] = f[i + 1][:]
        f[i][s[i]] = i
    q, = RI()
    for _ in range(q):
        t, = RS()
        i = -1
        for c in t:
            i = f[i + 1][ord(c) - ord('a')]
            if i == n:
                print(0)
                break
        else:
            print(suf[i + 1] + 1)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
