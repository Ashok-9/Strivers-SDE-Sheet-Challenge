from typing import List
def merge(arr, low, mid, high):
    temp = []   
    left = low   
    right = mid + 1  
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1    
    while left <= mid:
        temp.append(arr[left])
        left += 1 
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
def countPairs(arr, low, mid, high):
    c=0
    right = mid + 1
    left = low
    while left <= mid and right <= high:
        if arr[left] > 2*arr[right]:

            c += (mid - left + 1)
            right += 1
        else:

            left += 1
    print(c)
    return c
def mergeSort(arr, low, high):
    c=0
    if low >= high:
        return 0
    mid = (low + high) // 2
    c+=mergeSort(arr, low, mid)   
    c+=mergeSort(arr, mid + 1, high)   
    c+=countPairs(arr, low, mid, high)   
    merge(arr, low, mid, high)
    return c
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.c=0
        def merge(arr, low, mid, high):
            temp = []   
            left = low   
            right = mid + 1              
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1            
            while left <= mid:
                temp.append(arr[left])
                left += 1          
            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(low, high + 1):
                arr[i] = temp[i - low]
        def countPairs(arr, low, mid, high):
            right = mid + 1
            left = low
            while left <= mid and right <= high:
                if arr[left] > 2*arr[right]:

                    self.c += (mid - left + 1)
                    right += 1
                else:

                    left += 1
        def mergeSort(arr, low, high):
            
            if low >= high:
                return 0
            mid = (low + high) // 2
            mergeSort(arr, low, mid)   
            mergeSort(arr, mid + 1, high)   
            countPairs(arr, low, mid, high)   
            merge(arr, low, mid, high)
            return self.c
            
            
        return mergeSort(nums, 0, len(nums) - 1)


s = Solution()
nums = [2, 4, 3, 5, 1]
print(s.reversePairs(nums))
