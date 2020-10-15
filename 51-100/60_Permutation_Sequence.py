from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numStr = ''
        for i in range(1, n + 1):
            numStr += str(i)
        permutation = ''
        b = n
        while len(numStr) != 0:
            amount = self.getAmountOfNPermutation(b - 1)
            numIdx = k // amount
            if k % amount == 0:
                permutation += numStr[numIdx - 1]
                numStr = numStr[:numIdx - 1] + numStr[numIdx - 1 + 1:]
                k = amount
            else:
                permutation += numStr[numIdx]
                numStr = numStr[:numIdx] + numStr[numIdx + 1:]
                k = k - numIdx * amount
            if k == 0:
                break
            b -= 1
                

        return permutation + numStr[:]

    def getAmountOfNPermutation(self, n):
        amount = 1
        for i in range(1, n+1):
            amount *= i
        return amount

    def run(self):
        # print(self.getPermutation(3, 3))
        # print(self.getPermutation(4, 9))
        print(self.getPermutation(3, 2))

foo = Solution()
foo.run()
