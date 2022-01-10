from typing import List

"""
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
        Example 1:
        Input: numRows = 5
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # creating placeholder array with 1s to be iterated and modified later
        res = [[1]*(i+1) for i in range(numRows)]
        # print("before for", res)
        for i in range(2, numRows):
            for j in range(1, i):
                # print("inside second for --- i,j ---- ", i,j)
                # adding the res[i-1][j-1] + res[i-1][j]] as these are located above [i][j] and are adjacent
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res

result = Solution()
result.generate(5)