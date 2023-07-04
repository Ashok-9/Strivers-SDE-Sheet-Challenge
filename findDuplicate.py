from collections import defaultdict

def findDuplicate(arr:list, n:int):

    dic=defaultdict(int)
    for i in range(n):
        dic[arr[i]]+=1
    
    for i,j in dic.items():
        if j>1:
            return i

