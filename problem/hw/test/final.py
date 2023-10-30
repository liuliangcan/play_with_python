from collections import deque
from heapq import heappop, heappush
from math import inf

f = open('case2.in', 'r')
input = f.readline
"""大体思路:先把所有核切到最高算力，算有时间要求的任务(最差解)；然后用功耗最小的核慢慢算其他任务
1. 把所有cpu切到最高算力，这时计算一个平均算力avg；用这个avg来估算有时间要求的任务大约几点开始跑
2. 在反图上跑拓扑，每个任务的结束时间=min(后继任务的开始时间)；并计算所有任务的开始时间
3. 拓扑后，任务分成两类：有开始时间限制的，和无开始时间限制的。
4. 贪心地（这可能会导致无解）按照开始时间贪心地去依次执行任务，并且优先级高的先安排大核。同时计算总功耗。
5. 把功耗最低的最优核切到最低功耗，然后慢慢算无限制的任务
总体时间复杂度O(nlgn),瓶颈在排序
---
后续优化思路：
0. 如果算到中间发现无解，是否直接返回，反正也wa了。
1. 给出的3组样例直接特判打表出最优解。
2. 优化输入输出。
3. 由于复杂度充足，剩余时间是否尝试回溯（或其它较优解。
4. 如果数据量极小，尝试暴搜（重点优化思路

"""

#       ms
def solve():
    cpu_small_status, cpu_mid_status, cpu_big_status = [], [], []
    r, *cp = map(int, input().split())  # 长度和计算力+功耗
    best_cpu = [inf, inf, inf]  # 功耗最低的那个cpu状态(功耗,算力，cpu_id)
    for i in range(0, len(cp), 2):
        c, p = cp[i:i + 2]
        best_cpu = min(best_cpu, [p, c, 0])  # 找功耗最低的那个cpu和算力
        cpu_small_status.append(cp[i:i + 2])
    r, *cp = map(int, input().split())
    for i in range(0, len(cp), 2):
        c, p = cp[i:i + 2]
        best_cpu = min(best_cpu, [p, c, 6])
        cpu_mid_status.append(cp[i:i + 2])
    r, *cp = map(int, input().split())
    for i in range(0, len(cp), 2):
        c, p = cp[i:i + 2]
        best_cpu = min(best_cpu, [p, c, 7])
        cpu_big_status.append(cp[i:i + 2])

    cpu_small_status.sort(key=lambda x: x[0], reverse=True)  # 按算力降序排序
    cpu_mid_status.sort(key=lambda x: x[0], reverse=True)
    cpu_big_status.sort(key=lambda x: x[0], reverse=True)
    # print(cpu_small_status, cpu_mid_status, cpu_big_status)
    cpu_small, cpu_mid, cpu_big = cpu_small_status[0], cpu_mid_status[0], cpu_big_status[0]
    cpus = [cpu_small] * 4 + [cpu_mid] * 3 + [cpu_big]  # 把8个cpu都调到高算力
    # print(cpus)
    avg_comp = sum(c for c, _ in cpus) / 8  # 8个cpu平均算力

    n, m = map(int, input().split())
    tasks = []  # 输入任务
    s_cycles = 0  # 统计一共有多少工作量
    for _ in range(n):
        w, t = map(int, input().split())
        s_cycles += w
        tasks.append((w, t))
    # print(tasks)

    g = [[] for _ in range(n + 1)]  # 输入依赖关系
    rg = [[] for _ in range(n + 1)]  # 反图
    in_degree, out_degree = [0] * (n + 1), [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        rg[v].append(u)
        out_degree[u] += 1
        in_degree[v] += 1
    # 在反图上跑拓扑：计算有依赖关系的任务，建议什么时间开始执行
    task_start_time_sug = [inf] * (n + 1)  # 建议这个任务几点开始跑
    task_end_time_sug = [inf] * (n + 1)  # 建议这个任务几点结束
    for i, (_,t) in enumerate(tasks,start=1):  # 一定要提前更一下
        if t:
            task_end_time_sug[i] = t
    # print(deg)
    q = deque([i for i, v in enumerate(out_degree[1:], start=1) if v == 0])  # 这里入口应该可以只搞有时间限制的，能优化一点;哦不能这样做，会丢task
    while q:
        u = q.popleft()
        w, t = tasks[u - 1]  # u的任务量和要求结束时间
        task_start_time_sug[u] = task_end_time_sug[u] - w / avg_comp  # 用平均算力计算，建议几点开始(这里是否考虑用最低算力？
        for v in rg[u]:
            # print(u,v)
            task_end_time_sug[v] = min(task_end_time_sug[v], task_start_time_sug[u])  # v的结束时间<=u的开始时间
            out_degree[v] -= 1
            if out_degree[v] == 0:
                q.append(v)
    # print(deg)
    # print(task_start_time_sug)
    # print(task_end_time_sug)
    # 把任务分为两类：有建议开始时间的（有顺序），可以放到最后跑的
    ordered_tasks, other_tasks = [], []
    for i in range(1, n + 1):
        if task_start_time_sug[i] < inf:
            ordered_tasks.append((task_start_time_sug[i], i))
        else:
            other_tasks.append(i)
    ordered_tasks.sort()  # 把任务按建议开始时间排序

    h_cpu = [(0, -c, i) for i, (c, _) in enumerate(cpus)]  # cpu堆，(空闲时间，算力(取反)，cpu编号)
    h_cpu.sort()
    print(0, 2, 0, cpu_small[0])  # 先把三种核都切到最大算力
    print(0, 2, 6, cpu_mid[0])
    print(0, 2, 7, cpu_big[0])
    s_cost = 0  # 统计总功耗
    cur_time = 0
    for _, task_id in ordered_tasks:  # 在最大核上跑这些需要按时跑完的任务
        w, t = tasks[task_id - 1]  # 取出这个任务的计算量，要求完成时间
        st, c, cpu_id = heappop(h_cpu)  # 取出最早空闲的那个cpu
        cpu_p = cpus[cpu_id][1]  # 这个cpu的功耗水平
        c = -c
        print(st, 0, task_id, cpu_id)
        # print(cpu_p,w,c)
        s_cost += cpu_p * w / c  # 功耗*时间
        et = st + w / c  # 结束时间
        if t and et > t:
            print(f'无法完成任务{task_id},工作量{w},要求时间{t},实际时间{et},采用核为{cpu_id},算力{c}')
            return
        p = int(et) // 4 * 4  # cpu下次的可调度时间
        if et > p:
            p += 4
        cur_time = max(cur_time, p)
        heappush(h_cpu, (p, -c, cpu_id))

    # 在原图上跑拓扑，统计剩余任务的功耗
    cpu_p, c, cpu_id = best_cpu
    print(cur_time, 2, cpu_id, c)
    q = deque([i for i, v in enumerate(in_degree[1:], start=1) if v == 0 and task_start_time_sug[i] == inf])
    while q:
        u = q.popleft()
        w, _ = tasks[u - 1]
        # u直接在最好那个cpu上跑
        print(cur_time, 0, u, cpu_id)
        s_cost += cpu_p * w / c  # 计算功耗
        cur_time += w / c  # 注意整数和浮点型有转换，这里变成浮点
        p = int(cur_time) // 4 * 4
        if cur_time > p:
            p += 4
        cur_time = p  # 这里变成整数
    # print(s_cycles,s_cost)
    print(f"{s_cycles/s_cost:.3f}")



if __name__ == '__main__':
    solve()
