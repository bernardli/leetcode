from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 划分
        Zero = []
        positive = {}
        negative = {}
        result = []

        for i in nums:
            if i == 0:
                Zero.append(i)
            elif i > 0:
                if i not in positive:
                    positive[i] = 1
                else:
                    positive[i] += 1
            else:
                if i not in negative:
                    negative[i] = 1
                else:
                    negative[i] += 1

        posList = list(positive.keys())
        negList = list(negative.keys())

        # 0 0 0
        if len(Zero) >= 3:
            result.append([0, 0, 0])
        # - 0 + and - - +
        for i in range(len(negList)):
            # - 0 +
            if len(Zero) > 0 and -negList[i] in positive:
                result.append([negList[i], 0, -negList[i]])

            # - - +
            if negative[negList[i]] >= 2 and -negList[i] * 2 in positive:
                result.append([negList[i], negList[i], -negList[i] * 2])

            j = i + 1
            while j < len(negList):
                if -(negList[i] + negList[j]) in positive:
                    result.append([negList[i], negList[j], -
                                   (negList[i] + negList[j])])
                j += 1

        # - + +
        for i in range(len(posList)):
            if positive[posList[i]] >= 2 and -posList[i] * 2 in negative:
                result.append([-posList[i] * 2, posList[i], posList[i]])
            j = i + 1
            while j < len(posList):
                if -(posList[i] + posList[j]) in negative:
                    result.append(
                        [-(posList[i] + posList[j]), posList[i], posList[j]])
                j += 1

        return result

    def run(self):
        print(self.threeSum([-1, 0, 1, 2, -1, -4]))

        print(self.threeSum([3, 0, -2, -1, 1, 2]))
        print(self.threeSum([1,1,-2]))


foo = Solution()
foo.run()
