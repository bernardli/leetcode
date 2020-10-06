from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = 0
        idx = 0
        while idx < len(nums) - 1:
            maxPosition = 0
            selectIdx = 0
            for jumpDistance in range(1, nums[idx] + 1):
                if idx + jumpDistance < len(nums) - 1:
                    if nums[idx + jumpDistance] + idx + jumpDistance > maxPosition:
                        selectIdx = idx + jumpDistance
                        maxPosition = nums[idx + jumpDistance] + idx + jumpDistance
                else:
                    return step + 1
            step += 1
            idx = selectIdx

        return step

    def run(self):
        print(self.jump([2, 3, 1, 1, 4]))
        print(self.jump([1, 1, 1, 1]))
        print(self.jump([3, 2, 1]))
        print(self.jump([0]))
        print(self.jump([8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7, 0, 3, 4,
                         8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5]))


foo = Solution()
foo.run()
