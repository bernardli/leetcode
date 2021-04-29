class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s) + 1)]
        if len(s) == 0:
            return 1
        if s[0] == '0':
            dp[1] = 0
        else:
            dp[1] = 1
        dp[0] = 1

        for i in range(1, len(s)):
            if int(s[i-1:i+1]) >= 1 and int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) % 10 == 0:
                dp[i + 1] = dp[i - 1]
            elif int(s[i-1:i+1]) >= 1 and int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) % 10 != 0:
                if s[i-1] == '0':
                    dp[i + 1] = dp[i]
                    continue
                dp[i + 1] = dp[i] + dp[i - 1]
            elif int(s[i-1:i+1]) % 10 == 0:
                continue
            else:
                dp[i + 1] = dp[i]

        return dp[len(s)]

    def run(self):
        print(self.numDecodings('12'))
        print(self.numDecodings('226'))
        print(self.numDecodings('0'))
        print(self.numDecodings('06'))
        
        print(self.numDecodings('00'))
        print(self.numDecodings('2101'))
        print(self.numDecodings('10011'))
foo = Solution()
foo.run()