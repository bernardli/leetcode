from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        targetIndex = 0
        # find target
        while True:
            mid = (left + right) // 2
            if nums[mid] == target:
                targetIndex = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            if right < left:
                return [-1, -1]

        right_2 = targetIndex
        while True:
            mid = (left + right_2) // 2
            if nums[mid] == target:
                right_2 = mid - 1
            else:
                left = mid + 1
            if left > right_2:
                break

        left_2 = targetIndex
        while True:
            mid = (left_2 + right) // 2
            if nums[mid] == target:
                left_2 = mid + 1
            else:
                right = mid - 1
            if left_2 > right:
                break

        return [left, right]

    def run(self):
        print(self.searchRange([5, 7, 7, 8, 8, 10], 8))
        print(self.searchRange([5, 7, 7, 8, 8, 10], 6))


foo = Solution()
foo.run()
