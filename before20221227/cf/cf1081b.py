import collections
import io
import os
import sys

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
MOD = 10 ** 9 + 7


def solve(n, a):
    cnt = {n - k: v for k, v in collections.Counter(a).items()}  # 转化为几个数和它相同
    # {x:v} 相同次数出现的次数
    # 对于b[i] 来说有x个相同数在b里；每次消耗x个数，v也要消耗x个
    poses = collections.defaultdict(list)

    for i, x in enumerate(a):
        poses[n - x].append(i)

    i = 1
    ans = [0] * n
    for x, v in cnt.items():
        if v % x > 0:
            print('Impossible')
            return
        poss = poses[x]
        j = 0
        while v:
            for _ in range(x):
                ans[poss[j]] = i
                j += 1
            i += 1
            v -= x

    if len(ans) != n:
        print('Impossible')
        return

    print('Possible')
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    # print(n,a)
    solve(n, a)
