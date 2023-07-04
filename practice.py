def f(i):
    if i>=n-1:
        return []
    l1=[a[i]]+f(i+1)
    l2=f(i+1)
    return [l1]
    
a=[1,2,3,4]
n=len(a)
0
print(f(n))