import sys
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc221/tasks/abc221_e

【更新通知】
从今天开始，带你们刷 AtCoder 啦！

输入 n(≤3e5) 和长为 n 的数组 a (1≤a[i]≤1e9)。
输出有多少个 a 的长度至少为 2 的子序列，满足子序列的第一项 ≤ 子序列的最后一项。
由于答案很大，输出答案模 998244353 的结果。 

注：子序列不要求连续。

我的思考：寻找正序对(i,j) 即i<j 且 a[i]<=a[j]
        这个正序对 对答案的贡献有多少个序列呢，i..j中间有j-i-1个数，选或不选即2**(j-i-1)
        遍历到j时，寻找所有<=a[j]的数的下标集合，假设有k个i分别是 i1,i2,i3..ik
        ans += 2**(j-i1-1)+2**(j-i2-1)+..+2**(j-ik-1)
             = 2**(j-1) // 2**i1 + 2**(j-1) // 2**i2 +..+ 2**(j-1) // 2**ik
             = 2**(j-1) * inv(2**i1) + 2**(j-1) *inv(2**i2) +..+ 2**(j-1) *inv(2**ik)
             = 2**(j-1)*(inv(2**i1)+inv(2**i2)+..+inv(2**ik))
        也就是说遍历到j时，我们需要一个前边所有<=a[j]的值的(下标i的2的幂的逆元)的求和
        用树状数组维护每个数值的所有下标的幂逆元和

输入
3
1 2 1
输出 3
解释 [1,2], [1,1], [1,2,1]

输入
3
1 2 2
  1 2
1 2 4
输出 4
解释 [1,2], [1,2], [2,2], [1,2,2]

输入
3
3 2 1
输出 0

输入
10
198495780 28463047 859606611 212983738 946249513 789612890 782044670 700201033 367981604 302538501
输出 830
"""


def quick_pow_mod(a, b, p=MOD):
    ans = 1
    while b:
        if b & 1:
            ans = (ans * a) % p
        a = (a * a) % p
        b >>= 1
    return ans


class BinIndexTree:
    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            # self.a = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            # self.a = [0 for _ in range(self.size + 5)]
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_point(i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始
        # self.a[i] += v
        while i <= self.size:
            self.c[i] += v
            self.c[i] %= MOD
            # i += self.lowbit(i)
            i += i & -i

    # def set_point(self, i, v):  # 单点修改，下标从1开始 需要先计算差值，然后调用add
    #     self.add_point(i, v - self.a[i])
    #     self.a[i] = v
    #
    # def sum_interval(self, l, r):  # 区间求和，下标从1开始,计算闭区间[l,r]上的和
    #     return self.sum_prefix(r) - self.sum_prefix(l - 1)

    def sum_prefix(self, i):  # 前缀求和，下标从1开始
        s = 0
        while i >= 1:
            s += self.c[i]
            s %= MOD
            # i -= self.lowbit(i)
            i &= i - 1
        return s

    # def lowbit(self, x):
    #     return x & -x
    #
    # def print_a(self):
    #     print(self.a)


"""
寻找正序对(i,j) 即i<j 且 a[i]<=a[j]
这个正序对 对答案的贡献有多少个序列呢，i..j中间有j-i-1个数，选或不选即2**(j-i-1)
遍历到j时，寻找所有<=a[j]的数的下标集合，假设有k个i分别是 i1,i2,i3..ik
ans += 2**(j-i1-1)+2**(j-i2-1)+..+2**(j-ik-1)
     = 2**(j-1) // 2**i1 + 2**(j-1) // 2**i2 +..+ 2**(j-1) // 2**ik
     = 2**(j-1) * inv(2**i1) + 2**(j-1) *inv(2**i2) +..+ 2**(j-1) *inv(2**ik)
     = 2**(j-1)*(inv(2**i1)+inv(2**i2)+..+inv(2**ik))
也就是说遍历到j时，我们需要一个前边所有<=a[j]的值的(下标i的2的幂的逆元)的求和
用树状数组维护每个数值的所有下标的幂逆元和,则可以lg时间求出这个<=a[j]的前缀和
即ans += 2**(j-1)*tree.sum_prefix(a[j])
"""


#    412	 ms
def solve(n, a):
    h = sorted(set(a))
    n = len(h) + 1
    tree = [0] * (n + 1)
    ans = 0
    pwr2 = 1
    # inv2 = quick_pow_mod(2, MOD - 2, MOD)
    inv2 = (MOD + 1) // 2
    inv = 1
    for i, v in enumerate(a):
        x = bisect_left(h, v) + 1
        if i:
            p = x
            while p:
                ans = (ans + pwr2 * tree[p]) % MOD
                p &= p - 1
            pwr2 = pwr2 * 2 % MOD

        while x <= n:
            tree[x] += inv
            tree[x] %= MOD
            x += x & -x
        inv = inv * inv2 % MOD

    print(ans % MOD)


def main():
    n, = RI()
    a = RILST()
    solve(n, a)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """
3
2 3 1
""",
            """
5
"""
        ),
        (
            """
5
1 2 3 4 5
""",
            """
30
"""
        ),
        (
            """
8
8 2 7 3 4 5 6 1
""",
            """
136
"""
        )
    )
    if os.path.exists('test.test'):
        total_result = 'ok!'
        for i, (in_data, result) in enumerate(test_cases):
            result = result.strip()
            with io.StringIO(in_data.strip()) as buf_in:
                RI = lambda: map(int, buf_in.readline().split())
                RS = lambda: map(bytes.decode, buf_in.readline().strip().split())
                with io.StringIO() as buf_out, redirect_stdout(buf_out):
                    main()
                    output = buf_out.getvalue().strip()
                if output == result:
                    print(f'case{i}, result={result}, output={output}, ---ok!')
                else:
                    print(f'case{i}, result={result}, output={output}, ---WA!---WA!---WA!')
                    total_result = '---WA!---WA!---WA!'
        print('\n', total_result)
    else:
        main()
