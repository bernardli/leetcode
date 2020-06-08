from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestDiff = 10000 - (-1000)*3  # 根据题目给出的数值范围得出最差和结果
        threeSum = 0
        nums.sort()
        if len(nums) < 3:
            return None
        if len(nums) == 3:
            return sum(nums)
        for i in range(len(nums)):
            # 跳过重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum == target:
                    return curSum
                if abs(curSum - target) < closestDiff:
                    closestDiff = abs(curSum - target)
                    threeSum = nums[i] + nums[left] + nums[right]
                if curSum > target:
                    right -= 1
                else:
                    left += 1
        return threeSum

    def run(self):
        print(self.threeSumClosest([-1, 2, 1, -4], 1))

        print(self.threeSumClosest([1, 1, 1, 1], 0))


foo = Solution()
foo.run()
