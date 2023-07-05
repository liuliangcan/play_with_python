# MLE 对py太不友好


import array as arr

n, m = map(int, input().split())

a = arr.array('i', map(int, input().split()))
ans = 0
x = y = 0
l = s = 0
for r in range(n):
    s += a[r]
    while s > m:
        s -= a[l]
        l += 1
    if s > ans:
        ans = s
        x, y = l, r
print(x + 1, y + 1, ans)
