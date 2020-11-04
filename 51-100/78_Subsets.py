from typing import List
from copy import deepcopy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        maxLen = len(nums)
        self.result = []
        self.result.append([])

        for length in range(1, maxLen + 1):
            self.deepSearch(0, nums, length, [], 0)
        return self.result

    def deepSearch(self, startIdx, nums, length, subset, level):
        currSubset = deepcopy(subset)
        if level == length:
            self.result.append(currSubset)
            return

        for idx in range(startIdx, len(nums) - (length - level - 1)):
            self.deepSearch(idx + 1, nums, length,
                            currSubset + [nums[idx]], level + 1)

    def run(self):
        print(self.subsets([1, 2, 3]))

foo = Solution()
foo.run()