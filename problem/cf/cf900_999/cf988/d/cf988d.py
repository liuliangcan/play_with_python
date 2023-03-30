# Problem: D. Points and Powers of Two
# Contest: Codeforces - Codeforces Round 486 (Div. 3)
# URL: https://codeforces.com/contest/988/problem/D
# Memory Limit: 256 MB
# Time Limit: 4000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/988/problem/D

输入 n(≤1e5) 和长为 n 的整数数组 a(-1e9≤a[i]≤1e9)，没有相同元素。

从 a 中选择尽量多的数，组成集合 b，要求 b 中任意两个数的差的绝对值都是 2 的幂次。
输出 b 的大小以及 b 中的每个数。（没有顺序要求，多解输出任意一解）
输入
6
3 5 4 7 10 12
输出 
3
7 3 5

输入
5
-1 2 5 8 11
输出 
1
8
"""
"""结论题 数学+倍增枚举
acw63场T3
这题有个结论，答案数组长度最多是3，且是等差数列，公差d是2的幂次。
证明3的情况,即若d1、d2、d1+d2都是2的幂次，当且仅当d1=d2:
    排好序后假设数组是[a,b,c],差是d1,d2。且d1,d2都是2的幂次。
    那么什么情况下d1+d2也是2的幂次呢。
    从2进制考虑，d1和d2分别是只有一个1的二进制数，当且仅当他们相等的情况下，求和仅有一个1，且进位。
证明完3，第4个数无论如何都插入不进来了，它和第一个数的差是3倍公差，不是2的幂。
"""
"""https://codeforces.com/contest/988/submission/171194913

如果选两个数 x<y，那么枚举 k 寻找 y-x=2^k，做法类似两数之和。

如果选三个数 x<y<z，那么必须有 y-x=z-y=2^k，否则 z-x 不是 2 的幂次。做法同 2367. 算术三元组的数目

选四个是无法做到的，根据上面可知必须是等差数列，但这样最大-最小是 3*2^k，也不是 2 的幂次。
那么选大于四个数就更不可能了，因为相当于在四个数的基础上多了一个数，四个数不行就更别说大于四个数了。"""


#     421  ms
def solve1():
    n, = RI()
    a = set(RILST())
    mx = max(a)
    ans = [mx]
    for x in a:
        for k in range(33):
            if x + (1 << k) > mx:
                break
            t = [x]
            if (x + (1 << k)) in a:
                t.append(x + (1 << k))
            else:
                continue
            if (x + (1 << (k + 1))) in a:
                t.append(x + (1 << (k + 1)))
            if len(t) == 3:
                print(3)
                return print(*t)
            if len(t) > len(ans):
                ans = t[:]
    print(len(ans))
    print(*ans)


#   358    ms
def solve():
    n, = RI()
    a = set(RILST())
    mx = max(a)
    ans = [mx]
    for x in a:
        for k in range(33):
            t = x + (1 << k)
            if t > mx:
                break
            if t in a:
                ans = [x, t]
                if (x + (1 << (k + 1))) in a:
                    print(3)
                    return print(*ans, x + (1 << (k + 1)))

    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    solve()
