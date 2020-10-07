class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strLen = len(s)
        output = ''
        if numRows == 1:
            return s
        if numRows == 2:
            i = 0
            while i < strLen:
                output += s[i]
                i += 2
            i = 1
            while i < strLen:
                output += s[i]
                i += 2
            return output

        unitLen = numRows + (numRows - 2)  # 假设一竖一斜为一个单元
        remainsLen = strLen % unitLen

        # 输出第一行
        for i in range(int(strLen / unitLen) + min(1, remainsLen)):
            output += s[0 + i * unitLen]

        # 输出中间numRows-2行
        for lineIndex in range(1, numRows - 1):
            for i in range(int(strLen / unitLen)):
                output += s[lineIndex + i * unitLen]
                output += s[lineIndex +
                            ((numRows - (lineIndex + 1)) * 2 - 1 + 1) + i * unitLen]
            if min(1, max(0, remainsLen - (lineIndex + 1) + 1)) > 0:
                output += s[lineIndex +
                            int(strLen / unitLen) * unitLen]
            if min(1, max(0, remainsLen - (lineIndex + 1) - (numRows - (lineIndex + 1)) * 2 + 1)) > 0:
                output += s[lineIndex + ((numRows - (lineIndex + 1)) * 2 - 1 + 1) +
                            int(strLen / unitLen) * unitLen]

        # 输出最后一行
        for i in range(int(strLen / unitLen) + min(1, max(0, remainsLen - numRows + 1))):
            output += s[numRows - 1 + i * unitLen]

        return output

    def run(self):
        print(self.convert('LEETCODEISHIRING', 3))
        print(self.convert('LEETCODEISHIRING', 4))
        print(self.convert('PAYPALISHIRING', 3))
        print(self.convert('PAYPALISHIRING', 4))
        print(self.convert('PAYPALISHIRING', 2))
        print(self.convert('PAYPALISHIRING', 1))
        print(self.convert('PAYPAL', 4))
        


# test
foo = Solution()
foo.run()
