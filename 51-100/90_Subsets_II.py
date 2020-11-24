from typing import List
from copy import deepcopy

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.numPositionMap = dict()
        self.numCount = []
        self.positionNumMap = dict()
        for num in nums:
            if num not in self.numPositionMap:
                position = len(self.numPositionMap)
                self.numPositionMap[num] = position
                self.numCount.append(0)
                self.positionNumMap[position] = num

            self.numCount[self.numPositionMap[num]] += 1

        for subsetLen in range(len(nums) + 1):
            self.deep(subsetLen, 0, [])
        return self.result

    def deep(self, totalNumLen, position, subset):
        if totalNumLen == 0:
            self.result.append(subset)
            return
        if position == len(self.numCount):
            return
        oriSubset = deepcopy(subset)
        for currSubsetLen in range(self.numCount[position] + 1):
            if totalNumLen - currSubsetLen < 0:
                return
            
            newSubset = oriSubset + [self.positionNumMap[position]] * currSubsetLen
            self.deep(totalNumLen - currSubsetLen, position + 1, newSubset)

    def run(self):
        print(self.subsetsWithDup([1,2,2]))

foo = Solution()
foo.run()