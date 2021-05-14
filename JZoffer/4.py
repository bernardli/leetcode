from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n > 0:
            m = len(matrix[0])
        else:
            return False
        if m == 0:
            return False
        for i in range(n):
            rowIndex = n - i - 1
            if matrix[rowIndex][0] > target:
                continue
            elif self.binarySearch(0, m-1, matrix[rowIndex], target):
                return True
        return False

    def binarySearch(self, left, right, nums, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return True
        return False

    def run(self):
        print(self.findNumberIn2DArray([
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5))
        print(self.findNumberIn2DArray([
            [1,   4,  7, 11, 15],
            [2,   5,  8, 12, 19],
            [3,   6,  9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 20))

foo = Solution()
foo.run()
