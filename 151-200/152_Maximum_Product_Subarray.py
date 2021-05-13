from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = -float('inf')
        maxList = [0 for __ in range(len(nums))]
        minList = [0 for __ in range(len(nums))]
        maxList[0] = nums[0]
        minList[0] = nums[0]

        for i in range(1, len(nums)):
            maxList[i] = max(maxList[i-1] * nums[i], max(minList[i-1] * nums[i], nums[i]))
            minList[i] = min(maxList[i-1] * nums[i], min(minList[i-1] * nums[i], nums[i]))


        for i in range(len(maxList)):
            result = max(maxList[i], result)
        return result

    def run(self):
        print(self.maxProduct([2, 3, -2, 4]))
        print(self.maxProduct([-2, 0, -1]))

foo = Solution()
foo.run()
