from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, column = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == 0):
                    # adding the co-ordinates of the matrix which has zero to sets
                    row.add(i)
                    column.add(j)
        

        for zeroRow in row:
            self.setRowToZero(matrix, zeroRow)
        for zeroCol in column:
            self.setColToZero(matrix, zeroCol)
        
        #print(matrix)

    # make entire row to zero when zero found in whole matrix
    def setRowToZero(self, matrix, zeroRow):
        for element in range(len(matrix[zeroRow])):
            matrix[zeroRow][element] = 0

    # make entire column to zero when zero found in whole matrix
    def setColToZero(self, matrix, zeroCol):
        for element in range(len(matrix)):
            matrix[element][zeroCol] = 0

        

result = Solution()
result.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
result.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])