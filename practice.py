
import math

def nCr(n, r):
    res = 1

    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res

def pascalTriangle(n):
    for c in range(1, n+1):
        print(nCr(n-1, c-1), end=" ")
    print()

