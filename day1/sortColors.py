"""
    AKA DUCTH NATIONAL FLAG (DNF sort) ALGO
    AKA Sort an array of 0s, 1s and 2s (similar to quicksort)
    TC => O(n) => n is len(nums)
    SC => 0(1) => constant space used
"""

from typing import List

class Solution:
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


result = Solution()
result.sortColors([2,0,2,1,1,0])