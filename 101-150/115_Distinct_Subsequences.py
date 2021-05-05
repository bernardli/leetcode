class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for __ in range(len(t) + 1)] for __ in range(len(s) + 1)]
        
        for i in range(len(s) + 1):
            dp[i][len(t)] = 1
        
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                s_i = len(s) - i
                t_i = len(t) - j
                if s[s_i] == t[t_i]:
                    dp[s_i][t_i] = dp[s_i + 1][t_i + 1] + dp[s_i + 1][t_i]
                else:
                    dp[s_i][t_i] = dp[s_i + 1][t_i]

        return dp[0][0]

    def run(self):
        print(self.numDistinct('rabbbit', 'rabbit'))
        print(self.numDistinct('babgbag', 'bag'))

foo = Solution()
foo.run()