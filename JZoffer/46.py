class Solution:
    def translateNum(self, num: int) -> int:
        numStr = str(num)
        if len(numStr) == 1:
            return 1
        dp = [0 for i in range(len(numStr) + 1)]
        dp[1] = 1
        dp[0] = 1
        for i in range(1, len(numStr)):
            if i > 0 and int(numStr[i-1:i+1]) < 26 and int(numStr[i-1:i+1]) > 9:
                dp[i+1] += dp[i-1]
            dp[i+1] += dp[i]

        return dp[-1]

    def run(self):
        print(self.translateNum(12258))
        print(self.translateNum(27124))

        print(self.translateNum(506))
        print(self.translateNum(25))

foo = Solution()
foo.run()