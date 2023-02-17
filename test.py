import itertools
from functools import reduce
from math import gcd

if __name__ == '__main__':
    a = [1, 2, 3]
    n = len(a)
    ans = [0] * (2 * n)
    ans[1::2] = a
    print(ans)

    print(list(itertools.chain(*[(0, x) for x in a if x & 1 == 1])))
