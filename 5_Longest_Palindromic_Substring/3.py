'''
没想到这个最开始想到但觉得会太慢应该通过不了的思路居然通过了
仔细想想应该是因为不是每一个字符都满足左右展开进行判断的条件, 所以并不会每个字符都展开判断一遍
所以用时没有想想的长
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        maxHead = 0
        maxTail = 0
        self.totalLen = len(s)

        if self.totalLen == 0:
            return ''
        elif self.totalLen == 1:
            return s

        
        for i, c in enumerate(s):
            if i + 1 == self.totalLen:
                break
            if c == s[i + 1]:
                head, tail, length = self.isPalindromic(i, i + 1, s, 0)
                if length > maxLen:
                    maxLen = length
                    maxHead = head
                    maxTail = tail

            if i - 1 >= 0 and s[i - 1] == s[i + 1]:
                head, tail, length = self.isPalindromic(i - 1, i + 1, s, 1)
                if length > maxLen:
                    maxLen = length
                    maxHead = head
                    maxTail = tail

        return s[maxHead: maxTail + 1]

    def isPalindromic(self, left, right, s, length):
        while s[left] == s[right]:
            length += 2
            if left - 1 >= 0 and right + 1 <= self.totalLen - 1:
                left -= 1
                right += 1
            else:
                return left, right, length
        return left + 1, right - 1, length

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
