from typing import List
from copy import deepcopy


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.record = dict()  # tree
        self.maxLen = len(nums)
        self.result = []
        self.deepFirstSearch(nums, 0, [])
        return self.result

    def deepFirstSearch(self, nums, level, permutation):
        if level >= self.maxLen:
            return
        for i in range(len(nums)):
            currPermutation = deepcopy(permutation)
            currPermutation.append(nums[i])
            if len(currPermutation) == self.maxLen:
                if self.isNotDuplicate(currPermutation):
                    self.result.append(currPermutation)
            else:
                self.deepFirstSearch(
                    nums[:i]+nums[i+1:], level + 1, currPermutation)

    def isNotDuplicate(self, permutation):
        root = self.record
        Flag = False
        for num in permutation:
            if num not in root:
                root[num] = dict()
                Flag = True

            root = root[num]
        return Flag

    def run(self):
        print(self.permuteUnique([1, 1, 2]))


foo = Solution()
foo.run()
