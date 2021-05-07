from typing import List


class Solution:
    def minCut(self, s: str) -> List[List[str]]:
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

        dp_2 = [999 for __ in range(n)]
        for i in range(n):
            if dp[0][i] == True:
                dp_2[i] = 0
            else:
                for j in range(i):
                    if dp[j+1][i] == True:
                        dp_2[i] = min(dp_2[i], 1 + dp_2[j])

        return dp_2[n-1]

    def run(self):
        print(self.minCut('aab'))
        print(self.minCut('a'))
        print(self.minCut('ab'))


foo = Solution()
foo.run()
