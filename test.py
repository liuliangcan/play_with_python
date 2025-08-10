from itertools import permutations

good = {1}
for i in range(1<<10):
    p = []
    s = 0
    odd = 0
    for j in range(1,10):
        if i >>j & 1:
            p.append(j)
            s+=j
            if j &1:
                odd +=1
    if s > 16 or odd>=2:
        continue 
    mid = 0
    a = []
    for i in p:
        if i&1:
            mid = i
        a.extend([i]*(i//2))
    if mid:        
        if a:
            for c in permutations(a):
                good.add(int(''.join(map(str,list(c)+[mid]+list(c)[::-1]))))
    elif a:
        for c in permutations(a):
            good.add(int(''.join(map(str,list(c)+list(c)[::-1]))))
good = sorted(good)
print(len(good),good)