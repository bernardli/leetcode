from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        numsLen = len(nums)
        for i in range(numsLen):
            if nums[i] in record:
                return [record[nums[i]], i]
            else:
                record[target - nums[i]] = i

    def run(self):
        print(self.twoSum([2, 7, 11, 15], 0))


# test
foo = Solution()
foo.run()
