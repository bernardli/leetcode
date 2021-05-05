from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pathsCost = triangle.pop()
        # if len(triangle) == 0:    # 其实不需要这个, 因为只有一层的话就一个数, 不需要比大小
        #     return min(pathsCost)
        while len(triangle) != 0:
            path = triangle.pop()
            for i in range(len(path)):
                pathsCost[i] = min(pathsCost[i] + path[i],
                                   pathsCost[i+1] + path[i])
        return pathsCost[0]

    def run(self):
        print(self.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))

        print(self.minimumTotal([[2]]))

foo = Solution()
foo.run()
