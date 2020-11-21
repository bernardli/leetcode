class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return self.recursionCheck(s1, s2)

    def recursionCheck(self, s1, s2):
        if len(s1) == 1 and s1[0] == s2[0]:
            return True

        for divideIdx in range(1, len(s1)):
            flag1 = self.hasSameLetterSet(s1[:divideIdx], s2[:divideIdx])
            flag2 = self.hasSameLetterSet(s1[:divideIdx], s2[-divideIdx:])

            if flag1 and flag2:
                if  (
                        self.recursionCheck(s1[:divideIdx], s2[:divideIdx]) and
                        self.recursionCheck(s1[divideIdx:], s2[divideIdx:])
                    ) or (
                        self.recursionCheck(s1[:divideIdx], s2[-divideIdx:]) and
                        self.recursionCheck(s1[divideIdx:], s2[:-divideIdx])
                    ):
                    return True
            elif flag1:
                if self.recursionCheck(s1[:divideIdx], s2[:divideIdx]) and self.recursionCheck(s1[divideIdx:], s2[divideIdx:]):
                    return True
            elif flag2:
                if self.recursionCheck(s1[:divideIdx], s2[-divideIdx:]) and self.recursionCheck(s1[divideIdx:], s2[:-divideIdx]):
                    return True

        return False

    def hasSameLetterSet(self, s1, s2):
        s1Dict = dict()
        s2Dict = dict()

        for idx in range(len(s1)):
            if s1[idx] not in s1Dict:
                s1Dict[s1[idx]] = 1
            else:
                s1Dict[s1[idx]] += 1

            if s2[idx] not in s2Dict:
                s2Dict[s2[idx]] = 1
            else:
                s2Dict[s2[idx]] += 1

        for letter in s1Dict:
            if letter not in s2Dict:
                return False
            elif s1Dict[letter] != s2Dict[letter]:
                return False

        return True

    def run(self):
        print(self.isScramble('great', 'rgeat'))
        print(self.isScramble('abcde', 'caebd'))
        print(self.isScramble('a', 'a'))


foo = Solution()
foo.run()
