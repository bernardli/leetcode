class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''

        thousand = int(num / 1000)
        if thousand > 0:
            roman += 'M' * thousand
        
        num = num % 1000
        hundred = int(num / 100)
        if hundred < 4:
            roman += 'C' * hundred
        elif hundred == 4:
            roman += 'CD'
        elif hundred == 5:
            roman += 'D'
        elif hundred <9:
            roman += 'D' + 'C' * (hundred - 5)
        else:
            roman += 'CM'

        num = num % 100
        ten = int(num / 10)
        if ten < 4:
            roman += 'X' * ten
        elif ten == 4:
            roman += 'XL'
        elif ten == 5:
            roman += 'L'
        elif ten <9:
            roman += 'L' + 'X' * (ten - 5)
        else:
            roman += 'XC'

        num = num % 10
        if num < 4:
            roman += 'I' * num
        elif num == 4:
            roman += 'IV'
        elif num == 5:
            roman += 'V'
        elif num <9:
            roman += 'V' + 'I' * (num - 5)
        else:
            roman += 'IX'

        return roman

    def run(self):
        print(self.intToRoman(3))
        print(self.intToRoman(4))
        print(self.intToRoman(9))
        print(self.intToRoman(58))
        print(self.intToRoman(1994))

# test
foo = Solution()
foo.run()