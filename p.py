def f(i,prev):
    if i>=size-1:
        if (prev%2==0 and n[i]%2==0) or (prev%2!=0 and n[i]%2!=0):
            # print(n[i])
            return prev
        else:
            # print(n[i],prev,x)
            return prev-x
    if (prev%2==0 and n[i]%2==0) or (prev%2!=0 and n[i]%2!=0):
        t=f(i+1,n[i])
    else:       
        t=-x+f(i+1,n[i])

    nt=0+f(i+1,prev)
    print(t,nt)
    a=max(t,nt)
    return a
n=[2,3,6,1,9,2]
x=5
size=len(n)
print(f(1,n[0]))


# def f():
#     prev=n[0]
#     m=prev
#     ans=prev
#     for i in range(1,len(n)):
#         if (prev%2==0 and n[i]%2==0) or (prev%2!=0 and n[i]%2!=0):
#             m=m+n[i]
#             ans=max(m,ans)
#             prev=n[i]
           
            
#         else:
            # if m<m+n[i]-x:
            #     prev=n[i]
            #     m=m+n[i]-x
    #         m=m+n[i]-x
    #         ans=max(m,m+n[i]-x,ans)
    #         prev=n[i]
            
            
    # return ans
            