from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp = [False for __ in range(len(s) + 1)]
        # dp[0] = True
        wordLenSet = set()
        wordSet = set(wordDict)
        for word in wordDict:
            wordLenSet.add(len(word))
        subStrings = [[] for __ in range(len(s) + 1)]
        subStrings[0].append([''])

        for i in range(len(s)):
            for wordLen in wordLenSet:
                if i + 1 - wordLen < 0:
                    continue
                if len(subStrings[i + 1 - wordLen]) != 0 and s[i + 1 - wordLen:i + 1] in wordSet:
                    for subStr in subStrings[i + 1 - wordLen]:
                        temp = subStr[:]
                        temp.append(s[i + 1 - wordLen:i + 1])
                        subStrings[i + 1].append(temp)

        result = []
        for subStr in subStrings[len(s)]:
            temp = ''
            for word in subStr[1:]:
                temp += word + ' '
            result.append(temp[:-1])
        return result

    def run(self):
        print(self.wordBreak(s="catsanddog", wordDict=[
              "cat", "cats", "and", "sand", "dog"]))
        print(self.wordBreak(s="pineapplepenapple", wordDict=[
              "apple", "pen", "applepen", "pine", "pineapple"]))
        print(self.wordBreak(s="catsandog", wordDict=[
              "cats", "dog", "sand", "and", "cat"]))

foo = Solution()
foo.run()
