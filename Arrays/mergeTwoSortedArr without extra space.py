from typing import List
from math import ceil

class Solution:
    def mergeArrays(self, nums1:List[int], m:int, nums2:List[int], n:int) -> List[int]:
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]

    # def mergeArrays(self, nums1, m, nums2, n):
    #     for i in range(m):
    #         # take first element from arr1 
    #         # compare it with first element of second array
    #         # if condition match, then swap
    #         if nums1[i] > nums2[0]:
    #             nums1[i], nums2[0] = nums2[0], nums1[i]

    #     # then sort the second array
    #     # put the element in its correct position
    #     # so that next cycle can swap elements correctly
    #     first = nums2[0]
    #     # insertion sort is used here
    #     gen = (k for k in range(n) if nums2[k] < first)
    #     for k in gen:
    #         nums2[k-1] = nums2[k]
    #         nums2[k-1] = first

result = Solution()
result.mergeArrays([1,2,3,0,0,0], 3, [2,5,6], 3)