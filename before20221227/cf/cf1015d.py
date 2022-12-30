import os
import sys

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 10 ** 9 + 7


def solve(n, k, s):
    if not k <= s <= k * (n - 1):
        print('NO')
        return
    print('YES')
    ans = [1]
    while s > k:
        k -= 1
        if s - n + 1 >= k:
            s -= n - 1
            ans.append(n if ans[-1] == 1 else 1)
        else:
            t = s - k
            s -= t
            ans.append(1 + t if ans[-1] == 1 else n - t)
    while k:
        t = ans[-1]
        ans.append(t - 1 if t > 1 else t + 1)
        k -= 1
    print(' '.join(map(str, ans[1:])))


if __name__ == '__main__':
    n, k, s = map(int, input().split())
    solve(n, k, s)
