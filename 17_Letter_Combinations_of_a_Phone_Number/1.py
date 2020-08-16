from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = list()
        index = 0

        self.mapTable = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) < 1:
            return result

        self.level(index, '', digits, result)
        return result

    def level(self, index, combination, digits, result):
        if len(digits[index:]) < 1:
            result.append(combination)
            return
        for letter in self.mapTable[digits[index]]:
            self.level(index + 1, combination + letter, digits, result)

    def run(self):
        print(self.letterCombinations('23'))
        print(self.letterCombinations('847'))
        print(self.letterCombinations('22'))


foo = Solution()
foo.run()