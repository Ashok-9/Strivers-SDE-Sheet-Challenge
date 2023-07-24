
def f(i,s):
   
    if i>n:
        return 0
    if s>n:
        return 0
    if s==n:
        return 1
    if dp[i][s]!=-1:
        return dp[i][s]
    s+=(i+1)**x
    t=f(i+1,s)
    s-=(i+1)**x
    nt=f(i+1,s)
    dp[i][s]=nt+t
    return dp[i][s]
n=10
x=2
dp=[[-1]*(n+1) for i in range((n+1))]

print(f(0,0))