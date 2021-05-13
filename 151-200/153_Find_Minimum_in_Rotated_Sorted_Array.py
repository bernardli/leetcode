from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > minNum:
                continue
            else:
                return nums[i]
        return minNum

    def run(self):
        print(self.findMin([3, 4, 5, 1, 2]))
        print(self.findMin([4, 5, 6, 7, 0, 1, 2]))
        print(self.findMin([11, 13, 15, 17]))

foo = Solution()
foo.run()
