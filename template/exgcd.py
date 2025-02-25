""" 这里讲一些数论讲的很好：https://www.cnblogs.com/zjp-shadow/p/9267675.html
扩展欧几里得 exgcd
    先看一下欧几里得算法，即辗转相除法：
        gcd(a,b) = gcd(b,a%b)
            同时b=0时，返回a
    扩展gcd核心步骤用了这个类似的方法:
        exgcd(a,b) = exgcd(b,a%b)
            b=0时，返回1,0 （要求ab互质，否则还要算gcd；建议是把gcd放外边）
根据裴蜀定理 ax+by=1有解的条件是ab互质
那么ax+by=c有解的条件是 gcd(a,b)是c的因数。
我们把abc三个因数都除掉g=gcd(a,b),解集不变（因为等式两边可以同时乘除这个g)
这时我们先解ax+by=1这个式子，算完后再把x和y乘以c。
推导：
    ax+by   = 1
            = gcd(a,b)
            = gcd(b,a%b)
            = b*x' + a%b*y'
            = b*x' + (a-a//b*b)*y'
            = ay' + b(x'-a//b*y')
    对应一下,递推式是 x=y';y=x'-a//b*y'
    边界条件是b=0时返回1,0，证明：显然gcd(a,0)=a,即在b=0时，x=1,y=0可以得出a*1+b*0=1=gcd(a,b)
    最后得出一组解x0,y0,注意这个解是ax+by=1的解，别忘了x0*=c,y0*=c
    如何求解系呢，用不定方程求解,注意符号和系数：
        x=x0+tb
        y=y0-ta
    发现t可以任意变，随着t变大x变大且y变小；同时这也说明x和y大小关系也是相反的。
    根据这两个通解的式子，我们可以求正整数解（x,y均>0）的边界：
        比如要x>0,即x>=1
                    => x0+tb>=1
                    => t>=(1-x0)/b
  由于是大于所以向上取整=> t>=(1-x0+b-1)//b
            这时求出t=(b-x0)//b时，带入上述两个式子，x为正整数最小解，y为最大解；如果这时y<=0，那就没有正整数解。
        反之要y>0,即y>=1
                    => y0-ta>=1
                    => t<=(y0-1)/a
                    => t<=(y0-1)//a
            同上，这个t就是y最小正整数值，x最大值。
        注意这里两个例子是问正整数解，但很多题是求非负数解，一样的换一下公式即可：
            x>=0 => x0+tb>=0 => t>=(0-x+b-1)//b
            y>=0 => y0-ta>=0 => t<=y0//a
  显然，正整数解可能么有，有的话可以计数：
        求出ymin和ymax,则ycnt = (ymax-ymin)//a+1
用途：
    1. 求逆元，这里和费马小定理不同之处在于：
        费马小定理pow(x,mod-2,mod)要求mod是质数，而exgcd(a,b)只要求ab互质; 也因此中国剩余定理要用exgcd
        pow要跑满logMOD,exgcd可能快速下降
    注意!：x,y=exgcd(a,b)代表ax+by=1的一个解集，因此求出来的x是a在b上的逆元，但一定要做一步x%=b,因为是任意解可能为负
        即 1/a mod b = exgcd(a,b)[0]%b
    2. 线性同余，求一二元一次方程的整数解
例题：
    1. 判断是否有解、有正整数解、求正整数解上下界和个数：P5656 【模板】二元一次不定方程 (exgcd) https://www.luogu.com.cn/problem/P5656
    2. 求非负解集  https://www.luogu.com.cn/problem/UVA10090
"""
from math import gcd


def exgcd(a, b):  # 注意这里要求ab互质
    if b == 0:
        return 1, 0
    x1, y1 = exgcd(b, a % b)
    return y1, x1 - a // b * y1


def P5656():
    a, b, c = map(int, input().split())
    g = gcd(a, b)
    if c % g:  # g|c才有解
        return print(-1)
    a //= g
    b //= g
    c //= g
    x0, y0 = exgcd(a, b)  # 一组特解
    x0 *= c
    y0 *= c
    # 根据特解求ax+by=c的解系
    # x = x0+tb; y = y0-ta
    # x0+tb>0 => t> -x0/b  时取到x为正的最小值； y0-ta>0 => t<y0/a 时取到y为正的最小值
    ty = (y0 - 1) // a  # 此时y为最小整数
    tx = (1 - x0 + b - 1) // b  # 此时x为最小整数
    x = x0 + ty * b
    if x <= 0:  # x和y的最小解
        return print(x0 + tx * b, y0 - ty * a)
    # print(x0+tx*b)
    xmn = x0 + tx * b
    ymx = y0 - tx * a
    xmx = x0 + ty * b
    ymn = y0 - ty * a
    print((ymx - ymn) // a + 1, xmn, ymn, xmx, ymx)  # 正整数解的个数，最小值*2，最大值*2
