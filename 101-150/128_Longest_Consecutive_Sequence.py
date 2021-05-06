from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashTable = dict()
        result = dict()
        count = 0
        for num in nums:
            count += 1
            if num in hashTable:
                continue

            if num - 1 not in hashTable and num + 1 not in hashTable:   # 无接壤
                hashTable[num] = 1  # number
                result[num] = True
            elif num - 1 not in hashTable and num + 1 in hashTable:     # 右边接壤
                address = self.findAddress(num + 1, result, hashTable)
                hashTable[num] = address
                hashTable[address] += 1  # number
            elif num - 1 in hashTable and num + 1 not in hashTable:     # 左边接壤
                address = self.findAddress(num - 1, result, hashTable)
                hashTable[num] = address
                hashTable[address] += 1  # number
            elif num - 1 in hashTable and num + 1 in hashTable:         # 两边接壤
                leftAddress = self.findAddress(num - 1, result, hashTable)
                rightAddress = self.findAddress(num + 1, result, hashTable)
                hashTable[num] = leftAddress
                hashTable[leftAddress] += 1 + hashTable[rightAddress]
                hashTable[rightAddress] = leftAddress   # 右边指向左边
                del result[rightAddress]

        maxNum = 0
        for num in result:
            maxNum = max(maxNum, hashTable[num])

        return maxNum

    def findAddress(self, address, result, hashTable):
        while address not in result:
            address = hashTable[address]
        return address

    def run(self):
        print(self.longestConsecutive([100, 4, 200, 1, 3, 2]))
        print(self.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))

        print(self.longestConsecutive(
            [-3, 2, 8, 5, 1, 7, -8, 2, -8, -4, -1, 6, -6, 9, 6, 0, -7, 4, 5, -4, 8, 2, 0, -2, -6, 9, -4, -1]))


foo = Solution()
foo.run()
