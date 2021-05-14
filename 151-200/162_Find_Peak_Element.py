from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.divide(0, len(nums) - 1, nums)

    def divide(self, start, end, nums):
        if start == end:
            return start
        mid = (start + end) // 2
        if nums[mid] > nums[mid+1]:
            return self.divide(start, mid, nums)
        else:
            return self.divide(mid+1, end, nums)

    def run(self):
        print(self.findPeakElement([1, 2, 3, 1]))
        print(self.findPeakElement([1, 2, 1, 3, 5, 6, 4]))

foo = Solution()
foo.run()
