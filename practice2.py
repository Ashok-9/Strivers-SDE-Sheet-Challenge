import math
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        m=int(math.sqrt(n)+1)
        dp=[[-1]*(n+1) for i in range((m+1))]

        def f(i,s):

            if i>n:
                return 0
            if s>n:
                return 0
            if s==n:
                return 1
            if i>m:
                return 0
            if dp[i][s]!=-1:
                return dp[i][s]
            s+=(i+1)**x
            
            t=f(i+1,s)
            s-=(i+1)**x
            nt=f(i+1,s)
            dp[i][s]=nt+t
            return dp[i][s]
        # print(dp)
        return f(0,0)%(10**9+7)
s=Solution()
n=273
x=2
print(s.numberOfWays(n,x))
