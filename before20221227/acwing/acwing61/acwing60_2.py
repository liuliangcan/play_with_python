import io
import os
import sys
from collections import deque

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    m = len(arr)

    def dfs(index, s):
        if index == m:
            if s % 360 == 0:
                return True
            return False
        if dfs(index + 1, s + arr[index]):
            return True
        return dfs(index + 1, s - arr[index])


    print('YES' if  dfs(0, 0) else 'NO')
