from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        recordDict = dict()
        maxPositive = 0
        for num in nums:
            if num > 0:
                recordDict[num - 1] = True
                if num > maxPositive:
                    maxPositive = num

        for i in range(len(nums)):
            if i not in recordDict:
                return 1 + i
        return maxPositive + 1

    def run(self):
        print(self.firstMissingPositive([1, 2, 0])),
        print(self.firstMissingPositive([3, 4, -1, 1]))
        print(self.firstMissingPositive([7, 8, 9, 11, 12]))

foo = Solution()
foo.run()