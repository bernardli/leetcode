from typing import List

'''
a bad implement
'''

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        if n == 0:
            return [0]
        map = []
        for i in range(1, n + 1):
            scale = 2 ** (i - 1)
            map.append([0]*scale + [1]*scale + [1]*scale + [0]*scale)
        for idx in range(2 ** n):
            num = 0
            for i in range(n):
                num += map[i][idx % len(map[i])] * (2 ** i)
            result.append(num)
        return result

    def run(self):
        print(self.grayCode(2))
        print(self.grayCode(0))

foo = Solution()
foo.run()