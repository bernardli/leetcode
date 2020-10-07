from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.intervals = intervals
        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals
        while len(self.intervals) != 0:
            self.mergeTwoInterval()
        return self.result

    def mergeTwoInterval(self):
        # 把剩余的interval中最后一个拿出来, 和余下的比
        minNum, maxNum = self.intervals.pop()
        for idx in range(len(self.intervals)):
            leftEnd, rightEnd = self.intervals[idx]
            if minNum >= leftEnd and minNum <= rightEnd:
                self.intervals = self.intervals[:idx] + self.intervals[idx+1:]
                self.intervals.append([leftEnd, max(rightEnd, maxNum)])
                return
            elif maxNum >= leftEnd and maxNum <= rightEnd:
                self.intervals = self.intervals[:idx] + self.intervals[idx+1:]
                self.intervals.append([min(leftEnd, minNum), rightEnd])
                return
            elif minNum < leftEnd and maxNum > rightEnd:
                self.intervals = self.intervals[:idx] + self.intervals[idx+1:]
                self.intervals.append([minNum, maxNum])
                return
        self.result.append([minNum, maxNum])

    def run(self):
        print(self.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
        print(self.merge([[1, 4], [4, 5]]))


foo = Solution()
foo.run()
