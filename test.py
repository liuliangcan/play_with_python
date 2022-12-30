# !/usr/bin/env python
# -*- encoding: utf-8 -*-
from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        t = 2 ** n - 1
        vis = {(i, 1 << i) for i in range(n)}
        q = deque(vis)
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                u, mask = q.popleft()
                for v in graph[u]:
                    m = mask | (1 << v)
                    if m == t: return step
                    if (v, m) not in vis:
                        vis.add((v, m))
                        q.append((v, m))

        return 0
