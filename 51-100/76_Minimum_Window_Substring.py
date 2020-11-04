class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCount = dict()
        targetLeast = dict()
        for char in t:
            targetCount[char] = 0
            if char not in targetLeast:
                targetLeast[char] = 1
            else:
                targetLeast[char] += 1


        currMinLength = len(s) + 1
        currMinString = ''
        left, right = 0, 0
        flag = False
        while True:
            while right < len(s):
                if s[right] in targetCount:
                    targetCount[s[right]] += 1
                    if self.checkStatus(targetCount, targetLeast):
                        break
                right += 1

            if right >= len(s):
                right = len(s) - 1
                flag = True

            while left <= right:
                if s[left] not in targetCount:
                    left += 1
                    continue
                
                if self.checkStatus(targetCount, targetLeast) and right - left + 1 < currMinLength:
                    currMinLength = right - left + 1
                    currMinString = s[left: right + 1]
                targetCount[s[left]] -= 1
                if targetCount[s[left]] < targetLeast[s[left]]:
                    left += 1
                    break
                left += 1

            if flag:
                break
            right += 1
                    

        return currMinString

    def checkStatus(self, targetCount, targetLeast):
        for char in targetCount:
            if targetCount[char] < targetLeast[char]:
                return False
        return True
        

    def run(self):
        print(self.minWindow('ADOBECODEBANC', 'ABC'))
        print(self.minWindow('a', 'a'))

        print(self.minWindow('aa', 'aa')) # 忘了可以重复
        print(self.minWindow('bbaac', 'aba'))


foo = Solution()
foo.run()
