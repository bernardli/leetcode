'''
这一版的思路是记录每个字符出现的位置, 然后找左右两个字符相同的字段中间部分是否形成回文结构
但在重复字符的情况下(比如: aaaaaaaaaaa........)耗时很大, 没法通过
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.maxLen = 0
        self.charRecord = {}
        self.possibleStr = {}
        for i, c in enumerate(s):
            if c not in self.charRecord:
                self.charRecord[c] = [i]
            else:
                self.charRecord[c].append(i)
            self.countPossibleLen(i, c)
        
        possibleLens = list(self.possibleStr.keys())
        possibleLens.sort(reverse=True)

        for length in possibleLens:
            for head, tail in self.possibleStr[length]:
                if self.isPalindromic(head, tail, s):
                    return s[head:tail + 1]
        return ''
                

    def countPossibleLen(self, i, c):
        for index in self.charRecord[c]:
            length = i - index + 1
            if length not in self.possibleStr:
                self.possibleStr[length] = [[index, i]]
            else:
                self.possibleStr[length].append([index, i])

    def isPalindromic(self, head, tail, s):
        while head <= tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
                continue
            else:
                break
        if head < tail:
            return False
        else:
            return True


    def run(self):
        print(self.longestPalindrome('babad'))
        print(self.longestPalindrome('cbbd'))
        print(self.longestPalindrome('bb'))
        print(self.longestPalindrome('babadada'))
        print(self.longestPalindrome(''))
        print(self.longestPalindrome('abc'))
        print(self.longestPalindrome('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))


# test
foo = Solution()
foo.run()
