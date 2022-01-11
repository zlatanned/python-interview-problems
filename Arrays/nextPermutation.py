from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 0. To find next permutations, we'll start from the end
        i = j = len(nums)-1
        # 1. First we'll find the first non-increasing element starting from the end
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        # 2. After completion of the first loop, there will be two cases
            # 2.1. nums is in decreasing order
        if i == 0:
            nums.reverse()
            return 
        # 2.2. If it's not zero then we'll find the first number greater than nums[i-1] starting from end
        while nums[j] <= nums[i-1]:
            j -= 1
        # 3. Now out pointer is pointing at two different positions
        # i. first non-ascending number from end
        # j. first number greater than nums[i-1]
        
        # We'll swap these two numbers
        nums[i-1], nums[j] = nums[j], nums[i-1]
        
        # We'll reverse a sequence starting from i to end
        nums[i:]= nums[len(nums)-1:i-1:-1]

result = Solution()
result.nextPermutation([1,2,3])