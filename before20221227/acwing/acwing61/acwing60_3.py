import io
import os
import sys
from collections import deque

if os.getenv('LOCALTESTACWING'):
    sys.stdin = open('input.txt')


def sovle(R, x1, y1, x2, y2):
    if (y1 - y2) ** 2 + (x1 - x2) ** 2 >= R ** 2:
        return print("%.6f" % (x1 * 1.0), "%.6f" % (y1 * 1.0), "%.6f" % (R * 1.0))

    if x1 == x2 and y1 == y2:
        return print("%.6f" % ((x1 + R/2) ), "%.6f" % (y1 * 1.0), "%.6f" % (R / 2))

    c = ((y1 - y2) ** 2 + (x1 - x2) ** 2) ** 0.5

    c2 = c + R
    y3 = (y2 - c2 * (y2 - y1) / c)
    x3 = (x2 - c2 * (x2 - x1) / c)
    y4 = (y3 + y2) / 2
    x4 = (x3 + x2) / 2
    r = c2 / 2
    print("%.6f" % x4, "%.6f" % y4, "%.6f" % r)


if __name__ == '__main__':
    R, x1, y1, x2, y2 = map(int, input().split())
    sovle(R, x1, y1, x2, y2)
