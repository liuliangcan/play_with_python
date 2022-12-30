import collections
import io
import os
import sys
from collections import deque
from math import sqrt

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = sys.stdin.buffer.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7

"""
1. 模拟这个买糖果的过程，每次买一圈看看能买多少设为s，显然t>=s，那么一定可以转t//s圈，t本身减小到t%s;
2. 这里思考一下转t//s圈的前提是这几圈每圈数量不变：显然不会变大，因为上一圈没买到的贵的，下一圈钱也不可能够；也不会变小，因为t//s保证了每圈花的钱都可以是s。
3. 显然这几圈下来t%=s。对答案的贡献是圈数*买了几个糖：ans+=t//s*c
4. 计算一下复杂度，为什么不超时呢(n<2e5,t<1e18,1<=ai<=1e9)。
5. 显然循环内枚举每个店动作复杂度是O(n)。那么一共执行了多少次循环呢，观察退出循环的条件是s == 0。
6. s == 0只有一种可能，就是一圈店走下来，没有一个店<=t。则重点是t什么时候能降到足够小，即小于min(a)最差0。
7. 观察t的变化公式，每次t %= s。先说结论，t对一个小于t的数取模，t每次至少折半，因此复杂度是O(lgt)，总体复杂度是O(n*lgt)，lg1e18大概是63，因此不超时。
8. 证明为什么至少折半：
    我们知道s<=t, 等于的情况不说了，t%s=0。
                当s>=t//2, 即s在t一半的右边，t%s = t-s < t//2
                当s<=t//2, t//s >= 2，取模一定<s,显然小于t。
    因此t对小于t的数取模，至少折半 
"""
def solve(n, t, a):
    ans = 0

    while True:
        s = 0
        c = 0
        for x in a:
            if s + x <= t:
                s += x
                c += 1
        if s == 0:
            break
        ans += t // s * c
        t %= s
    print(ans)


if __name__ == '__main__':
    n, t = RI()
    a = RILST()
    solve(n, t, a)
