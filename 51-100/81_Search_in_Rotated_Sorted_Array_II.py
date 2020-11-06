from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         return True
        #     # if nums[(left + mid) // 2] <= nums[mid]:
        #     if nums[left] <= nums[mid]:
        #         if target < nums[mid] and target >= nums[left]:
        #             return self.binarySearch(left, mid - 1, nums, target)
        #         else:
        #             left = mid + 1
        #     # elif nums[(mid + right) // 2] >= nums[mid]:
        #     elif nums[right] >= nums[mid]:
        #         if target > nums[mid] and target <= nums[right]:
        #             return self.binarySearch(mid + 1, right, nums, target)
        #         else:
        #             right = mid - 1
        if len(nums) == 0:
            return False
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        priorNum = nums[left]
        if priorNum == target:
            return True
        for idx in range(left + 1, mid):
            if nums[idx] == target:
                return True
            if nums[idx] < priorNum:
                return self.binarySearch(idx + 1, right, nums, target)
        for idx in range(mid + 1, len(nums)):
            if nums[idx] == target:
                return True

        return False

    def binarySearch(self, left, right, nums, target):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return False

    def run(self):
        # print(self.search([2, 5, 6, 0, 0, 1, 2], 0))
        # print(self.search([2, 5, 6, 0, 0, 1, 2], 3))

        # print(self.search([3, 1], 1))
        # print(self.search([3, 1, 1, 1, 1], 3))
        # print(self.search([1, 3, 1, 1, 1], 3))
        # print(self.search([1, 3], 3))
        print(self.search([10, 10, 10, -10, -10, -10, -10, -9, -9, -9, -9, -9, -9, -9, -8, -8, -8, -8, -8, -8, -8, -8, -7, -7, -7, -7, -6, -6, -6, -5, -5, -5, -4, -4, -4, -4, -3, -3, -2, -2, -2, -2, -
                           2, -2, -2, -2, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 10, 10], -6))


foo = Solution()
foo.run()
