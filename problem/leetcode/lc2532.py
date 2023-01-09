from heapq import *
from typing import List

# https://leetcode.cn/problems/time-to-cross-a-bridge/
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        l, r, t1, t2 = [], [], [], []
        for i, (lr, po, rl, pn) in enumerate(time):
            heappush(l, (-lr - rl, -i))
        ans = 0  # 桥空下来的时间
        while True:
            while t1 and t1[0][0] <= ans:  # 当前时间桥左侧都有谁等待
                _, i = heappop(t1)
                heappush(l, (-time[i][0] - time[i][2], -i))
                print(1)
            while t2 and t2[0][0] <= ans:  # 当前时间桥右侧都有谁等待
                _, i = heappop(t2)
                heappush(r, (-time[i][0] - time[i][2], -i))
                print(2)
            if not r and (not l or not n):
                print(3)
                ans = 1e9
                if t1:
                    ans = t1[0][0]
                if t2:
                    ans = min(ans, t2[0][0])
                continue
            print(ans,l,r,t1,t2)
            if r:  # 当前时间如果桥右侧有人等，就让他走
                _, i = heappop(r)
                i = -i
                ans = ans + time[i][2]
                heappush(t1, (ans + time[i][3], i))  # 这个人加入左侧等待队伍
            elif n:  # 右侧没人等待，还有箱子，左侧才上桥
                _, i = heappop(l)
                i = -i
                ans = ans + time[i][0]
                heappush(t2, (ans + time[i][1], i))
                n -= 1
            if not n and not r and not t2:  # 如果箱子没了，且右侧没人等了
                break
        return ans

n = 1
k = 3
time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
print(Solution().findCrossingTime(n,k,time))