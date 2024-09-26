"""https://orac2.info/problem/aiio12negotiations/"""
import sys
from itertools import accumulate

from sortedcontainers import SortedList

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

def solve():
    n, = RI()
    k, = RI()
    a = []
    for _ in range(n):
        v, = RI()
        a.append(v)
    pre = [0] + list(accumulate(a))

    def ok(x):
        sl = SortedList()
        cnt = 0
        for v in pre:
            cnt += sl.bisect_right(v-x)
            sl.add(v)
        return cnt < k
    l, r = 0, pre[-1]+1
    while l+1<r:
        mid = (l+r)>>1
        if ok(mid):
            r = mid
        else:
            l = mid
    print(l)
    # print(bisect_left(range(pre[-1]+1),True,key=ok)-1)  # RE


solve()


