from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])

        rowIdx = 0
        colIdx = 0
        rightEnd = n
        bottomEnd = m
        leftEnd = -1
        topEnd = 0
        result = []

        while True:
            while colIdx < rightEnd:
                result.append(matrix[rowIdx][colIdx])
                colIdx += 1
            if rowIdx == bottomEnd - 1 and colIdx == rightEnd:
                break
            else:
                colIdx -= 1
                rowIdx += 1
                rightEnd -= 1

            while rowIdx < bottomEnd:
                result.append(matrix[rowIdx][colIdx])
                rowIdx += 1
            if colIdx == leftEnd + 1 and rowIdx == bottomEnd:
                break
            else:
                rowIdx -= 1
                colIdx -= 1
                bottomEnd -= 1

            while colIdx > leftEnd:
                result.append(matrix[rowIdx][colIdx])
                colIdx -= 1
            if rowIdx == topEnd + 1 and colIdx == leftEnd:
                break
            else:
                colIdx += 1
                rowIdx -= 1
                leftEnd += 1

            while rowIdx > topEnd:
                result.append(matrix[rowIdx][colIdx])
                rowIdx -= 1
            if colIdx == rightEnd - 1 and rowIdx == topEnd:
                break
            else:
                rowIdx += 1
                colIdx += 1
                topEnd += 1

        return result

    def run(self):
        print(self.spiralOrder([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]))

        print(self.spiralOrder([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]))

foo = Solution()
foo.run()
