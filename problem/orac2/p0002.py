"""https://orac2.info/problem/aiio12negotiations/"""
import os.path
import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
INFILE = 'teamin.txt'
OUTFILE = 'teamout.txt'
if INFILE and os.path.exists(INFILE):
    sys.stdin = open(INFILE, 'r')
if INFILE and os.path.exists(INFILE):
    sys.stdout = open(OUTFILE, 'w')
"""求约瑟夫环倒数4个人
"""


def JosephusLastM(n, k, m):
    """约瑟夫环,n个人报数到k的人出队，问倒数第m个人的编号(1~n)"""
    winner = (k - 1) % m
    for i in range(m + 1, n + 1):
        winner = (winner + k) % i
    return winner + 1


def solve():
    n, k = RI()

    print(' '.join(map(str, [JosephusLastM(n, k, i) for i in range(4, 0, -1)])))


solve()

sys.stdout.close()
