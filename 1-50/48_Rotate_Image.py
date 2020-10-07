from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        maxLevel = n // 2
        
        for level in range(maxLevel):
            idx = level
            while idx < n - level - 1:
                top = matrix[level][idx]
                right = matrix[idx][n - level - 1]
                bottom = matrix[n - level - 1][n - idx - 1]
                left = matrix[n - idx - 1][level]

                matrix[level][idx] = left
                matrix[idx][n - level - 1] = top
                matrix[n - level - 1][n - idx - 1] = right
                matrix[n - idx - 1][level] = bottom
                idx += 1

        print(matrix)

    def run(self):
        self.rotate([[1,2,3],[4,5,6],[7,8,9]])
        self.rotate([0])
        self.rotate([[1,2],[3,4]])

foo = Solution()
foo.run()