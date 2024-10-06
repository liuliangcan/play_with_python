"""获取数组中的数组对，gcd恰好为k的对的个数。记为res[k]。O(n+UlgU)
本质是DP。
先统计a中每个元素的cnt。
枚举k及其倍数2k,3k...,累计个数记为c。
这c个数中任两个数的GCD一定是k的倍数，所以c*(c-1)//2就是GCD等于k、2k、3k..的数量。
但我们要计算恰好等于k的个数，所以要减去2k、3k、4k的个数，即res[2k],res[3k]..
得：res[k] = c*(c-1)//2-res[2k]-res[3k]..
可以看到均从大的转移而来，而且转移花费符合调和级数O(UlgU)。

应用：
- cf1884d https://codeforces.com/problemset/problem/1884/D 询问有多少对不存在公因数在数组里，那么直接求恰好的gcd，然后如果gcd的因数不在数组里即可贡献这对
- https://leetcode.cn/problems/sorted-gcd-pair-queries/  lc418T4，问第k小gcd是几，求出res后前缀和+二分


"""


def gcd_pair_cnt(a):
    mx = max(a)
    cnt = [0]*(mx+1)
    for v in a:
        cnt[v] += 1
    res = [0]*(mx+1)
    for i in range(mx,0,-1):
        c = 0
        for j in range(i,mx+1,i):
            c += cnt[j]
            res[i] -= res[j]
        res[i] += c*(c-1)//2
    return res