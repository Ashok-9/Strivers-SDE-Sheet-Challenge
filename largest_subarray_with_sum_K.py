from collections import defaultdict
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    ts=0
    dic=defaultdict(int)
    n=len(a)
    m=float('-inf')
    for i in range(n):
        ts+=a[i]
        if not ts in dic:
            dic[ts]=i
        
        rem=ts-k
        if ts==k:
            m=i+1
        elif rem in dic :
            print(i,dic[rem])
            m=max(m,i-dic[rem])
    print(dic)
    return m
n,k=map(int,input().split())
a=list(map(int,input().split()))

print(longestSubarrayWithSumK(a,k))