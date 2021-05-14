class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for __ in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], dp[i-j] * j, (i - j) * j)

        return dp[n]

    def run(self):
        print(self.cuttingRope(2))
        print(self.cuttingRope(10))

foo = Solution()
foo.run()