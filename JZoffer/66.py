from typing import List


class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        left = [1 for _ in range(len(a))]
        right = [1 for _ in range(len(a))]
        for i in range(len(a)):
            if i >0:
                left[i] = left[i-1] * a[i]
                right[-(i+1)] = right[-(i+1)+1] * a[-(i+1)]
            else:
                left[i] = a[i]
                right[-(i+1)] = a[-(i+1)]

        result = []
        for i in range(len(a)):
            if i == 0:
                result.append(right[i+1])
            elif i == len(a) - 1:
                result.append(left[i-1])
            else:
                result.append(left[i-1] * right[i+1])

        return result
            

    def run(self):
        print(self.constructArr([1, 2, 3, 4, 5]))


foo = Solution()
foo.run()
