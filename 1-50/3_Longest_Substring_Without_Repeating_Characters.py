class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        substring = list()
        maxLen = 0
        currentLen = 0
        for c in s:
            if c not in record:
                record[c] = True
                substring.append(c)
                currentLen += 1
                if currentLen > maxLen:
                    maxLen = currentLen
            else: 
                while substring[0] != c:
                    del record[substring[0]]
                    substring.pop(0)
                    currentLen -= 1
                substring.pop(0)
                substring.append(c)
                
        return maxLen
        
    def run(self):
        print(self.lengthOfLongestSubstring('abcabcbb'))
        print(self.lengthOfLongestSubstring('bbbbb'))
        print(self.lengthOfLongestSubstring('pwwkew'))
        print(self.lengthOfLongestSubstring('dvdf'))
        print(self.lengthOfLongestSubstring('aab'))
        print(self.lengthOfLongestSubstring('ckilbkd'))


# test
foo = Solution()
foo.run()
            