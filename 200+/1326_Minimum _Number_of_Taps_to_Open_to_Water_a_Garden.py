from typing import List


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rightMost = [i for i in range(n + 1)]
        for idx in range(n + 1):
            leftEnd = max(0, idx - ranges[idx])
            rightMost[leftEnd] = max(idx + ranges[idx], rightMost[leftEnd])

        tapCount = 0
        searchLeft = 0
        searchRight = 0
        while searchRight < n:
            tapCount += 1
            newSearchRight = -1
            for idx in range(searchLeft, searchRight+1):
                newSearchRight = max(rightMost[idx], newSearchRight)
                
            if newSearchRight == searchRight: # 说明有断点
                return -1

            searchLeft = searchRight
            searchRight = newSearchRight
        
        return tapCount
            

    def run(self):
        print(self.minTaps(5, [3, 4, 1, 1, 0, 0]))
        print(self.minTaps(3, [0, 0, 0, 0]))
        print(self.minTaps(7, [1, 2, 1, 0, 2, 1, 0, 1]))
        print(self.minTaps(8, [4, 0, 0, 0, 0, 0, 0, 0, 4]))
        print(self.minTaps(8, [4, 0, 0, 0, 4, 0, 0, 0, 4]))


foo = Solution()
foo.run()
