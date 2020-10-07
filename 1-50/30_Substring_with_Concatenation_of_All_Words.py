from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return list()

        self.wordLen = len(words[0])
        self.wordsNum = len(words)
        self.wordDict = dict()
        self.str = s
        result = list()

        for word in words:
            if word not in self.wordDict:
                self.wordDict[word] = 1
            else:
                self.wordDict[word] += 1

        for index in range(int(len(s)) - self.wordLen * self.wordsNum + 1):
            if s[index:index + self.wordLen] in self.wordDict:
                if self.isSubString(index):
                    result.append(index)

        return result

    def isSubString(self, startIndex):
        tempDict = dict()
        for key in self.wordDict:
            tempDict[key] = self.wordDict[key]

        for p in range(self.wordsNum):
            index = startIndex + p * self.wordLen
            word = self.str[index: index + self.wordLen]
            if word in tempDict and tempDict[word] > 0:
                tempDict[word] -= 1
            else:
                return False

        return True

    def run(self):
        print(self.findSubstring("barfoothefoobarman", ["foo", "bar"]))
        print(self.findSubstring("wordgoodgoodgoodbestword",
                                 ["word", "good", "best", "word"]))


foo = Solution()
foo.run()
