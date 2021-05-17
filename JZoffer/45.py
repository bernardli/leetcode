from typing import List
import functools


def cmp(x, y):
    str1 = x + y
    str2 = y + x
    if str1 > str2:
        return 1
    elif str1 < str2:
        return -1
    else:
        return 0


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        numStrs = [str(num) for num in nums]
        sortedNumStrs = sorted(numStrs, key=functools.cmp_to_key(cmp))
        result = ''
        for numStr in sortedNumStrs:
            result += numStr
        return result

    def run(self):
        print(self.minNumber([10, 2]))
        print(self.minNumber([3, 30, 34, 5, 9]))


foo = Solution()
foo.run()

# def reversed_cmp(x, y):
#     if x > y:
#         return -1
#     if x < y:
#         return 1
#     return 0


# sorted([36, 5, 12, 9, 21], key=reversed_cmp)
