t = input()
s = input()
m, n = len(t), len(s)
# if not t:
#     print(n)
t = t[::-1]
s = s[::-1]
j = 0
for i, c in enumerate(s):
    if j < m and c == t[j]:
        j += 1
        if j == m:
            print(n - i - 1)
            exit(0)
else:
    print(-1)
