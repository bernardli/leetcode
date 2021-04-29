from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        vaildResult = []
        self.recursion(0, 0, s, [], vaildResult)
        return vaildResult

    def recursion(self, currNum, currLen, s, currResult, vaildResult):
        for numLen in range(1,4):
            if len(s) - currLen - numLen < 4 - currNum - 1 or len(s) - currLen - numLen > (4 - currNum - 1) * 3:
                continue
            
            currStr = s[currLen:currLen+numLen]
            if self.isValid(currStr):
                currResult.append(currStr)
                if currNum + 1 == 4:
                    vaildResult.append(self.arrToString(currResult))
                else:
                    self.recursion(currNum + 1, currLen + len(currStr), s, currResult, vaildResult)
                currResult.pop()
    
    def isValid(self, subStr):
        if len(subStr) > 1 and subStr[0] == '0':
            return False
        elif int(subStr) > 255:
            return False
        return True

    def arrToString(self, arr):
        result = ''
        for subString in arr:
            result += subString + '.'
        return result[:-1]

    def run(self):
        print(self.restoreIpAddresses('25525511135'))
        print(self.restoreIpAddresses('0000'))
        print(self.restoreIpAddresses('1111'))
        print(self.restoreIpAddresses('010010'))
        print(self.restoreIpAddresses('101023'))

foo = Solution()
foo.run()