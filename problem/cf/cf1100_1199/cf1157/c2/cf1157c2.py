# Problem: C2. Increasing Subsequence (hard version)
# Contest: Codeforces - Codeforces Round 555 (Div. 3)
# URL: https://codeforces.com/problemset/problem/1157/C2
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
PROBLEM = """https://codeforces.com/problemset/problem/1157/C2

输入 n(1≤n≤2e5) 和长为 n 的双端队列 a(1≤a[i]≤2e5)。
每次操作，弹出 a 的队首或队尾。
从第二次操作开始，弹出的数字必须严格大于上一次弹出的数字。
输出最多可以弹出多少个数字，以及操作序列（队首为 L，队尾为 R）。
输入
5
1 2 4 3 2
输出 
4
LRRR

输入
7
1 3 5 6 5 4 2
输出
6
LRLRRR

输入
3
2 2 2
输出
1
R

输入
4
1 2 4 3
输出
4
LLRR
"""


#   108    ms
def solve():
    n, = RI()
    a = RILST()
    l, r = 0, n - 1
    ans = []
    cur = 0  # 1<=a[i]
    while l <= r and (a[l] > cur or a[r] > cur):
        if cur < a[l] < a[r] or a[r] <= cur < a[l]:  # 用l优或者只能用l
            cur = a[l]
            ans.append('L')
            l += 1
        elif a[l] > a[r] > cur or a[l] <= cur < a[r]:  # 用r优或者只能用r
            cur = a[r]
            ans.append('R')
            r -= 1
        else:  # 两端相等，则选了一端后不能再用另一端，只能从这边一直向后了，选更长那边
            left = right = 1
            while l + 1 < n and a[l] < a[l + 1]:
                l += 1
                left += 1
            while r - 1 >= 0 and a[r] < a[r - 1]:
                r -= 1
                right += 1
            ans.extend('L' * left if left > right else 'R' * right)
            break
    print(len(ans))
    print(''.join(ans))
#   155    ms
def solve3():
    n, = RI()
    a = RILST()
    l, r = 0, n - 1
    ans = []
    cur = 0  # 1<=a[i]
    while l <= r and (a[l] > cur or a[r] > cur):
        if cur < a[l] < a[r] or a[r] <= cur < a[l]:  # 用l优或者只能用l
            cur = a[l]
            ans.append('L')
            l += 1
        elif a[l] > a[r] > cur or a[l] <= cur < a[r]:  # 用r优或者只能用r
            cur = a[r]
            ans.append('R')
            r -= 1
        else:  # 两端相等，则选了一端后不能再用另一端，只能从这边一直向后了，选更长那边
            left = right = 1
            while l + 1 < n and a[l] < a[l + 1]:
                l += 1
                left += 1
            while r - 1 >= 0 and a[r] < a[r - 1]:
                r -= 1
                right += 1
            ans.extend('L' * left if left > right else 'R' * right)
            break
    print(len(ans))
    print(*ans, sep='')


#   186    ms
def solve1():
    n, = RI()
    a = RILST()
    left, right = [1] * n, [1] * n  # 每个位置作为左/右出发点能走多远，
    for i in range(n - 2, -1, -1):
        if a[i] < a[i + 1]:
            left[i] += left[i + 1]
    for i in range(1, n):
        if a[i] < a[i - 1]:
            right[i] += right[i - 1]
    l, r = 0, n - 1
    ans = []
    cur = 0  # 1<=a[i]
    while l <= r:
        if max(a[l], a[r]) <= cur:  # 动不了了
            break
        if cur < a[l] < a[r] or a[r] <= cur < a[l]:  # 用l优或者只能用l
            cur = a[l]
            ans.append('L')
            l += 1
        elif a[l] > a[r] > cur or a[l] <= cur < a[r]:  # 用r优或者只能用r
            cur = a[r]
            ans.append('R')
            r -= 1
        else:  # 两端相等，则选了一端后不能再用另一端，只能从这边一直向后了，选更长那边
            if left[l] > right[r]:
                cur = a[l]
                ans.append('L')
                l += 1
            else:
                cur = a[r]
                ans.append('R')
                r -= 1
    print(len(ans))
    print(*ans, sep='')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
