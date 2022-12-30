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


"""哥德巴赫猜想：任意大于5的整数都可以写成3个质数之和。n>5,当n是偶数，n=n-2+2,n-2也是偶数，可以分解成2个质数的和；当n是奇数，n=n-3+3,n-3是偶数
偶数的哥德巴赫猜想：任意大于2的偶数都可以写成2个质数之和；比如4=2+2，6=3+3,8=3+5；如果n>4，则可以分解成两个奇质数的和。
奇数的哥德巴赫猜想：任意大于7的奇数都可以写成3个奇质数之和；比如9=3+3+3,11=3+3+5,这是因为可以直接-3；7本身-3就是4了。
关于本题，
如果n是质数答案是1。
否则如果n是偶数，注意到这一步，偶数是从4开始的，那满足偶数的哥德巴赫猜想，因此可以分解成2个质数，这两个数的贡献分别是1，答案是2。
否则如果n是奇数，注意到这一步，奇数是从9开始的，则满足奇数的哥德巴赫猜想，因此可以分解成3个奇质数，答案最多是3；但是要先判断一下，如果n-2是质数，则可以分解成2和一个奇质数，答案是2
"""
def solve():
    n, = RI()
    def is_zhishu(x):
        for i in range(2, int(sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    if is_zhishu(n):
        return print(1)

    if n & 1 == 0 or is_zhishu(n-2):
        return print(2)
    print(3)

if __name__ == '__main__':
    solve()
