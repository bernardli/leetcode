from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        self.n = len(ratings)
        minCandyNum = [-1 for __ in range(self.n)]
        for i in range(self.n):
            self.checkLeastCandy(i, minCandyNum, ratings)
        return sum(minCandyNum)

    def checkLeastCandy(self, i, minCandyNum, ratings):
        if minCandyNum[i] != -1:
            return minCandyNum[i]

        leftLeast = 0
        rightLeast = 0
        if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
            leftLeast = self.checkLeastCandy(i - 1, minCandyNum, ratings)
        if i + 1 < self.n and ratings[i] > ratings[i + 1]:
            rightLeast = self.checkLeastCandy(i + 1, minCandyNum, ratings)
        minCandyNum[i] = max(leftLeast, rightLeast) + 1
        return minCandyNum[i]

    def run(self):
        print(self.candy([1, 0, 2]))
        print(self.candy([1, 2, 2]))

foo = Solution()
foo.run()
