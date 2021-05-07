from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False for __ in range(n)] for __ in range(n)]
        for strLen in range(n):
            for start in range(n):
                if start + strLen >= n:
                    break
                end = start + strLen
                if strLen == 0:
                    dp[start][end] = True
                elif strLen == 1:
                    dp[start][end] = (s[start] == s[end])
                else:
                    dp[start][end] = (dp[start+1][end-1]
                                      and s[start] == s[end])

        result = []
        self.recursion(0, dp, s, n, result, [])
        return result

    def recursion(self, start, dp, s, n, result, preResult):
        for strLen in range(n - start):
            currResult = preResult[:]
            if dp[start][start + strLen] == True:
                currResult.append(s[start:start+strLen+1])

                if start + strLen == n - 1:
                    result.append(currResult)
                else:
                    self.recursion(start + strLen + 1, dp, s, n, result, currResult)

    def run(self):
        print(self.partition('aab'))
        print(self.partition('a'))

foo = Solution()
foo.run()
