import datetime
import random
from bisect import bisect_left
from heapq import heappush, heappop
"""尝试构造输入数据
1. 构造三种cpu。
2. 构造n个任务,随机任务计算量。
3. 把8个cpu和空闲时间扔到堆里，顺序跑这些任务，记录完成时间。
4. 按照完成时间，后完成的就可以依赖先完成的，构造边。
5. 输出任务时，随机给一些任务附加关键属性，要求时间则是实际完成时间+rand(1,5)
"""
cpu_cnt = [4, 3, 1]
r_limit = 3
rs = [random.randint(2, r_limit), random.randint(2, r_limit), random.randint(2, r_limit)]

cpu_status = [[] for _ in range(3)]
fz, fm = 90, 8
for i in range(3):
    for _ in range(rs[i]):
        dz = random.randint(10, 20)
        dy = fm * dz // fz + 1
        fz += dz  # 算力，功耗
        fm += dy
        cpu_status[i].append((fz, fm, fz / fm))

for i, v in enumerate(cpu_status):
    print(len(v), v)

cpus = []  # 8个cpu的算力，都取第二强的频点
for _ in range(4):
    c, _, _ = cpu_status[0][1]
    cpus.append(c)
for _ in range(3):
    c, _, _ = cpu_status[1][1]
    cpus.append(c)
for _ in range(1):
    c, _, _ = cpu_status[2][1]
    cpus.append(c)

n = random.randint(9, 20)  # 有多少个任务
task = []
for _ in range(n):
    task.append(random.randint(300, 800))  # 每个任务的量
print(n, task)
h = [(0, c, i) for i, c in enumerate(cpus)]  # 空闲时间和cpu
h.sort()
time = 0
result = []  # 第i个任务第几秒分配给了谁，啥时候完成,工作量
for i, w in enumerate(task):
    t, c, cpu_id = heappop(h)
    bt = int(t) // 4 * 4  # 小于t的那个4的倍数
    if t > bt:  # 如果超过了，则下一个4秒才能使用这个cpu
        bt += 4
    result.append((bt, cpu_id, bt + w / c, w))
    heappush(h, (bt + w / c, c, i))
print(result)
# 按开始执行的时间分组任务，那么后边的时间可以依赖前边的时间,result是按顺序分配任务，因此开始时间是有序的，二分进行random
# m = random.randint(1, n*(n+1)//2)  # 边数
m = random.randint(1, 5)
edges = []
keys_task = set()
for _ in range(m):
    while True:
        v = random.randint(0, n - 1)
        if result[v][0] != 0:
            p = bisect_left(result, (result[v][0], 0, 0, 0)) - 1
            if p >= 0:
                u = random.randint(0, p)
                edges.append((u + 1, v + 1))
                keys_task.add(v)
                break
print(m, edges)

t = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # 输出到文件
filename = f'{t}.in'
with open(filename, 'w+') as f:
    for i, v in enumerate(cpu_status):
        p = [len(v)]
        for c, cc, _ in v:
            p.extend([c, cc])
        f.write(' '.join(map(str, p)) + '\n')
    f.write(f'{n} {m}\n')
    for i, (bt, cpu_id, et, w) in enumerate(result):
        k = random.randint(0, 1)  # 1是关键任务，给个期限
        if k:
            k = int(et) + random.randint(1,5)  # 完成时间可以向后一点
        f.write(f'{w} {k}\n')
    for u, v in edges:
        f.write(f'{u} {v}\n')
