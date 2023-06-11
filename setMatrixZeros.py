from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:

    row=False
    col=False
    m=len(matrix)
    n=len(matrix[0])
    for i in range(n):
        if matrix[0][i]==0:
            col=True
    for i in range(m):
        if matrix[i][0]==0:
            row=True
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if row==True:
        for i in range(m):
            matrix[i][0]=0
    if col==True:
        for i in range(n):
            matrix[0][i]=0
    return matrix