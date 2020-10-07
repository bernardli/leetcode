'''
a bad implement
'''
from typing import List
from copy import deepcopy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        solution = []
        maxCombinationLen = target // candidates[0]

        self.deep(candidates, target, solution, [])
        checkDict = dict()
        result = []
        for combination in solution:
            if self.isUnique(combination, checkDict):
                result.append(combination)

                tempDict = dict()
                for num in combination:
                    if num not in tempDict:
                        tempDict[num] = 1
                    else:
                        tempDict[num] += 1

                checkDict[len(checkDict)] = deepcopy(tempDict)

        return result

    def deep(self, candidates, currentSum, solution, combination):
        for num in candidates:
            combination.append(num)

            if currentSum - num > 0:
                self.deep(candidates, currentSum - num, solution, combination)
            elif currentSum - num == 0:
                solution.append(deepcopy(combination))
                combination.pop()
                break
            else:
                combination.pop()
                break

            combination.pop()

    def isUnique(self, combination, checkDict):
        for i in checkDict:
            if not self.isNotEqual(checkDict[i], combination):
                return False
        return True

    def isNotEqual(self, countDict, combination):
        if set(countDict.keys()) != set(combination):
            return True
        tempDict = dict()
        for num in combination:
            if num not in tempDict:
                tempDict[num] = 1
            else:
                tempDict[num] += 1

        for num in countDict:
            if countDict[num] != tempDict[num]:
                return True

        return False

    def run(self):
        print(self.combinationSum([2, 3, 6, 7], 7))
        print(self.combinationSum([2, 3, 5], 8))


foo = Solution()
foo.run()
