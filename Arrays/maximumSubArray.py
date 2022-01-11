"""
    AKA KADANE'S ALGO
    TC => O(n) => n is len(nums)
    SC => 0(1) => constant space used
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum, max_sum = float('-inf'), float('-inf')
        for i in range(len(nums)):
            current_sum = max(0, current_sum)
            current_sum += nums[i]
            max_sum = max(current_sum, max_sum)
        # print(max_sum)
        return max_sum

        

result = Solution()
result.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])