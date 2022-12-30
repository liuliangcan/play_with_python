import io
import os
import sys
from collections import deque

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    if n <= m and n <= k:
        print('Yes')
    else:
        print('No')
