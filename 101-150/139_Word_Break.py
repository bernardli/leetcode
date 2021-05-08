from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = [[False for __ in range(len(wordDict))]
        #       for __ in range(len(wordDict))]
        dp = [False for __ in range(len(s) + 1)]
        dp[0] = True
        wordLenSet = set()
        wordSet = set(wordDict)
        for word in wordDict:
            wordLenSet.add(len(word))

        for i in range(len(s)):
            for wordLen in wordLenSet:
                if i + 1 - wordLen < 0:
                    continue
                if dp[i + 1 - wordLen] == True and s[i + 1 - wordLen:i + 1] in wordSet:
                    dp[i + 1] = True
                    break
        return dp[len(s)]

    def run(self):
        print(self.wordBreak('leetcode', ["leet", "code"]))
        print(self.wordBreak('applepenapple', ["apple", "pen"]))
        print(self.wordBreak('catsandog', [
              "cats", "dog", "sand", "and", "cat"]))

        print(self.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
                             ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))


foo = Solution()
foo.run()
