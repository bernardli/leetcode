class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}
        numsLen = len(nums)
        for i in range(numsLen):
            if i <= target:
                if (target - nums[i]):
                    return [record[target - nums[i]], i]
                else:
                    record[target - nums[i]] = i