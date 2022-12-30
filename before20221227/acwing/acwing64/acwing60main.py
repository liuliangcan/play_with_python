import io
import os
import sys
from collections import deque

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
else:
    input = sys.stdin.readline
MOD = 998244353

def main():
    a = 1

    def changfe(b):
        nonlocal a
        a += b

    changfe(10)
    print(a)

if __name__ \
        == '__main__':
    main()

