from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line = 0
        currLineWords = []
        currLeastLen = 0
        currLineIntervalNum = 0
        wordIdx = 0
        result = []
        while wordIdx < len(words):
            word = words[wordIdx]
            wordLen = len(word)
            if len(currLineWords) == 0:
                currLineWords.append(word)
                currLeastLen += wordLen
                wordIdx += 1
            elif len(currLineWords) != 0 and wordLen + currLeastLen + 1 <= maxWidth:
                currLineWords.append(word)
                currLeastLen += wordLen + 1
                currLineIntervalNum += 1
                wordIdx += 1
            else:
                wordStr = self.justifyLine(
                    currLineWords, currLineIntervalNum, maxWidth)
                result.append(wordStr)
                line += 1
                currLineWords.clear()
                currLeastLen = 0
                currLineIntervalNum = 0
            
        # last line
        wordStr = ''
        for idx in range(len(currLineWords)):
            wordStr += currLineWords[idx]
            if idx < currLineIntervalNum:
                wordStr += ' '
        wordStr += ' ' * (maxWidth - len(wordStr))
        result.append(wordStr)
        return result

    def justifyLine(self, currLineWords, currLineIntervalNum, maxWidth):
        pureWordLen = 0
        for word in currLineWords:
            pureWordLen += len(word)
        totalIntervalLen = maxWidth - pureWordLen
        space = []
        wordStr = ''
        for idx in range(currLineIntervalNum):
            space.append(' ' * (totalIntervalLen // currLineIntervalNum))
            if idx < totalIntervalLen % currLineIntervalNum:
                space[idx] += ' '
        for idx in range(len(currLineWords)):
            wordStr += currLineWords[idx]
            if idx < len(space):
                wordStr += space[idx]
        wordStr += ' ' * (maxWidth - len(wordStr))  
        return wordStr

    def run(self):
        print(self.fullJustify(
            ["This", "is", "an", "example", "of", "text", "justification."], 16))
        print(self.fullJustify(["What", "must", "be",
                                "acknowledgment", "shall", "be"], 16))
        print(self.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
                                "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))


foo = Solution()
foo.run()
