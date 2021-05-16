from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        result = []
        self.n = len(s)
        self.recursion(s[:], '', result)
        return result

    def recursion(self, s, currStr, result):
        if len(currStr) == self.n:
            result.append(currStr)
            return
        hashRecord = dict()
        for i in range(len(s)):
            char = s[i]
            if char in hashRecord:
                continue
            hashRecord[char] = True
            self.recursion(s[:i] + s[i+1:], currStr + char, result)

    def run(self):
        print(self.permutation('abc'))
        print(self.permutation('abb'))

foo = Solution()
foo.run()