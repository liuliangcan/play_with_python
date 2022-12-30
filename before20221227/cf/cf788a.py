import os
import sys

# from itertools import pairwise
from math import inf

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # diff = [abs(a - b) for a, b in pairwise(arr)]
    diff = [abs(arr[i] - arr[i + 1]) for i in range(n - 1)]


    def solve(l):
        ma = dp = -inf
        sign = 1
        for i in range(l, n - 1):
            dp = diff[i] * sign if dp <= 0 else dp + diff[i] * sign
            ma = max(ma, dp)
            sign *= -1
        return ma


    print(max(solve(0), solve(1)))
