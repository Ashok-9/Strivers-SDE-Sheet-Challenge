
from typing import List
import math


def merge(arr: List[int], low: int, mid: int, high: int) -> int:
    global cnt
    temp = []
    left = low
    right = mid + 1

    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)
            right += 1

    while (left <= mid):
        temp.append(arr[left])
        left += 1

    while (right <= high):
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]
    # print(cnt)
    return cnt


cnt = 0


def mergeSort(arr: List[int], low: int, high: int) -> int:
    global cnt

    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)
    print(cnt)


def numberOfInversions(a: List[int], n: int) -> int:

    n = len(a)

    return mergeSort(a, 0, n - 1)


a = [5, 4, 3, 2, 1]
n = 5
numberOfInversions(a, n)

print("The number of inversions are:", cnt)
