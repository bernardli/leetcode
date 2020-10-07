from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        result = []
        minNum, maxNum = newInterval
        idx = 0
        newLeftEnd = -1
        newRightEnd = -1
        priorRightEnd = -1
        while idx < len(intervals):
            leftEnd, rightEnd = intervals[idx]
            if minNum > rightEnd:
                result.append(intervals[idx])
            elif minNum >= leftEnd and minNum < rightEnd:
                newLeftEnd = leftEnd
                break
            elif minNum == rightEnd:
                newLeftEnd = leftEnd
                idx += 1
                break
            elif minNum < leftEnd:
                newLeftEnd = minNum
                break
            idx += 1

        if len(result) == len(intervals):
            result.append(newInterval)
            return result

        while idx < len(intervals):
            leftEnd, rightEnd = intervals[idx]
            if maxNum <= rightEnd and maxNum > leftEnd:
                newRightEnd = max(rightEnd, maxNum)
                result.append([newLeftEnd, newRightEnd])
                idx += 1
                break
            elif maxNum < leftEnd:
                newRightEnd = maxNum
                result.append([newLeftEnd, newRightEnd])
                break
            elif maxNum == leftEnd:
                newRightEnd = rightEnd
                result.append([newLeftEnd, newRightEnd])
                idx += 1
                break

            idx += 1

        if newRightEnd == -1:
            result.append([newLeftEnd, max(maxNum, priorRightEnd)])
            return result

        while idx < len(intervals):
            result.append(intervals[idx])
            idx += 1

        return result

    def run(self):
        print(self.insert([[1, 3], [6, 9]], [2, 5]))
        print(self.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
        print(self.insert([], [5, 7]))
        print(self.insert([[1, 5]], [2, 3]))
        print(self.insert([[1, 5]], [2, 7]))

        print(self.insert([[1, 5]], [0, 3]))


foo = Solution()
foo.run()
