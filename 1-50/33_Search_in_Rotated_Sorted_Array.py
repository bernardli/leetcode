from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length == 0:
            return -1
        right = length - 1
        left = 0
        while True:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[0]:
                if nums[0] <= target and  target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and target <= nums[length - 1]:
                    left = mid + 1
                else:
                    right = mid - 1
            if left > right:
                break

        return -1



    def run(self):
        print(self.search([4, 5, 6, 7, 0, 1, 2], 3))
        print(self.search([3, 1], 1))
        print(self.search([5, 1, 3], 0))


foo = Solution()
foo.run()
