from sys import exit

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B = B[::-1]

# Find match
need_swap = [i for i in range(n) if A[i] == B[i]]

if len(need_swap) == 0:
    print("Yes")
    print(" ".join(map(str, B)))
    exit()

val = A[need_swap[0]]
for i in range(n):
    if len(need_swap) == 0:
        break
    if A[i] != val and B[i] != val:
        j = need_swap.pop()
        B[i], B[j] = B[j], B[i]
if len(need_swap) == 0:
    print("Yes")
    print(" ".join(map(str, B)))
else:
    print("No")
