import io
import os
import sys
from collections import deque

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        a,b,c = map(int, input().split())
        print((a+b+c)//2)

