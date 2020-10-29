from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False

        rowIdx = 0
        while rowIdx < len(matrix):
            if target == matrix[rowIdx][0] or target == matrix[rowIdx][len(matrix[0]) - 1]:
                return True
            elif matrix[rowIdx][0] < target and target < matrix[rowIdx][len(matrix[0]) - 1]:
                break
            else:
                rowIdx += 1

        if rowIdx == -1:
            return False
        if rowIdx == len(matrix):
            return False

        # 二分查找
        left, right = 0, len(matrix[0])
        mid = (left + right) // 2
        while left <= right:
            if matrix[rowIdx][mid] == target:
                return True
            elif matrix[rowIdx][mid] < target:
                left = mid + 1
            elif matrix[rowIdx][mid] > target:
                right = mid - 1
            mid = (left + right) // 2
        return False

    def run(self):
        print(self.searchMatrix(
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
        print(self.searchMatrix(
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 13))
        print(self.searchMatrix([], 0))

foo = Solution()
foo.run()
