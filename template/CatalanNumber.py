"""卡特兰数
数列的前几项为：1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862 ：https://zhuanlan.zhihu.com/p/97619085
https://blog.csdn.net/sherry_yue/article/details/88364746
https://blog.csdn.net/weixin_44520881/article/details/105437210

递推公式： f[0] = f[1] = 1
公式1： f[n]=f[0]f[n-1]+f[1]f[n-2]+...+f[n-1]f[0]
公式2： f[n]=f[n−1]∗(4∗n−2)/(n+1)
通项公式
公式3： f[n]=C(2n,n)/(n+1)(n=0,1,2,...)
公式4： f[n]=C(2n,n)−C(2n,n−1)
"""

# 打印前 n 个卡特兰数
ans, n = 1, 20
print("1:" + str(ans))
for i in range(2, n + 1):
    ans = ans * (4 * i - 2) // (i + 1)
    print(str(i) + ":" + str(ans))