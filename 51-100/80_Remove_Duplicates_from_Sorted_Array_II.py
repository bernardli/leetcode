from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        currNum = nums[0]
        currNumCount = 1
        tailPointer = 0
        for idx in range(1, len(nums)):
            if nums[idx] == currNum:
                currNumCount += 1
            else:
                currNum = nums[idx]
                currNumCount = 1

            if currNumCount <= 2:
                tailPointer += 1
                nums[tailPointer] = nums[idx]

        return tailPointer + 1

    def run(self):
        print(self.removeDuplicates([1, 1, 1, 2, 2, 3]))
        print(self.removeDuplicates([0,0,1,1,1,1,2,3,3]))

foo = Solution()
foo.run()
