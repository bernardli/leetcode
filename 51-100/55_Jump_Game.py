from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == 0:
                return False
            maxPosition = 0
            selectIdx = 0
            for jumpDistance in range(1, nums[idx] + 1):
                if idx + jumpDistance < len(nums) - 1:
                    if nums[idx + jumpDistance] + idx + jumpDistance > maxPosition:
                        selectIdx = idx + jumpDistance
                        maxPosition = nums[idx +
                                           jumpDistance] + idx + jumpDistance
                else:
                    return True
            idx = selectIdx

        return True

    def run(self):
        print(self.canJump([2, 3, 1, 1, 4]))
        print(self.canJump([3, 2, 1, 0, 4]))

foo = Solution()
foo.run()