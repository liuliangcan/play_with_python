import collections
import os
import sys
from collections import Counter
from functools import lru_cache

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
# else:
#     input = sys.stdin.readline
MOD = 10 ** 9 + 7

@lru_cache
def solve(s):
    ans = []
    d = []
    stack = 0
    for c in s:
        if c == '(':
            stack += 1
        elif c == ')':
            if stack > 0:
                stack -= 1
            else:
                if not d:
                    return print(-1)
                ans[d[-1]] -= 1
                if ans[d[-1]] <= 1:
                    d.pop()
        else:
            if stack > 0:
                ans.append(stack)
                if stack > 1:
                    d.append(len(ans) - 1)
                stack = 0
            else:
                if not d:
                    return print(-1)
                ans.append(1)
                ans[d[-1]] -= 1
                if ans[d[-1]] <= 1:
                    d.pop()
    if stack > 0:
        return print(-1)
    print('\n'.join(map(str, ans)))
    # print(''.join(f'{a}\n' for a in ans))


if __name__ == '__main__':
    s = input()
    solve(s)
