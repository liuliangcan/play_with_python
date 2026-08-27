from cmath import log
from itertools import permutations
from math import log2

# good = {1}
# for i in range(1<<10):
#     p = []
#     s = 0
#     odd = 0
#     for j in range(1,10):
#         if i >>j & 1:
#             p.append(j)
#             s+=j
#             if j &1:
#                 odd +=1
#     if s > 16 or odd>=2:
#         continue
#     mid = 0
#     a = []
#     for i in p:
#         if i&1:
#             mid = i
#         a.extend([i]*(i//2))
#     if mid:
#         if a:
#             for c in permutations(a):
#                 good.add(int(''.join(map(str,list(c)+[mid]+list(c)[::-1]))))
#     elif a:
#         for c in permutations(a):
#             good.add(int(''.join(map(str,list(c)+list(c)[::-1]))))
# good = sorted(good)
# print(len(good),good)

print(log(18) / log(1.1) / 2)
print((1.1 ** 15) * (1.1 ** 15))

BASE = random.getrandbits(32) | 131
MOD = 10 ** 9 + 7
N = 5 * 10 ** 5 + 5
p = [1] * N
for i in range(1, N):
    p[i] = p[i - 1] * BASE % MOD

h = [0] * (N + 1)


def get(l, r):
    return (h[r + 1] - h[l] * p[r - l + 1]) % MOD


class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        ans = set()
        for w in words:
            s = w[::2] + w[::2]
            n = len(s) // 2
            for i in range(1, n * 2 + 1):
                h[i] = (h[i - 1] * BASE + ord(s[i - 1])) % MOD
            p1 = min(get(i, i + n - 1) for i in range(n))

            s = w[1::2] + w[1::2]
            n = len(s) // 2
            for i in range(1, n * 2 + 1):
                h[i] = (h[i - 1] * BASE + ord(s[i - 1])) % MOD
            p2 = min(get(i, i + n - 1) for i in range(n)) if n else 0

            ans.add(p1 << 32 | p2)
        return len(ans)
