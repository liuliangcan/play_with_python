import io
import os
import sys
from collections import deque

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    diff = [a[0]]
    for i in range(1, n):
        diff.append(a[i] - a[i - 1])
    j = 0
    for _ in range(k):
        while j<n and diff[j] == 0:
            j += 1
        if j >= n:
            print(0)
        else:
            print(diff[j])
            diff[j] = 0

