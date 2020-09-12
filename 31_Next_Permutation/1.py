from typing import List
import heapq


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return None
        # 如果已经是最大
        if self.isMax(nums):
            temp = sorted(nums)
            # 这里如果直接写nums=sorted(nums)的话, 本地能输出正确结果, 但leetcode里不能
            for i in range(len(temp)):  
                nums[i] = temp[i]
            print(nums)
            return None

        h_max = list()
        heapq.heappush(h_max, -nums[-1])
        changedNum = 0
        changedIndex = 0
        for i in range(2, len(nums)+1):
            if nums[-i] >= -h_max[0]:
                heapq.heappush(h_max, -nums[-i])
            else:
                heapq.heappush(h_max, -nums[-i])
                changedNum = nums[-i]
                changedIndex = len(nums) - i
                break

        h_min = list()
        nextNum = -heapq.heappop(h_max)
        for i in range(len(h_max)):
            if -h_max[0] == changedNum:
                break
            else:
                heapq.heappush(h_min, nextNum)
                nextNum = -heapq.heappop(h_max)
        

        for i in range(len(h_max)):
            heapq.heappush(h_min, -heapq.heappop(h_max))

        nums[changedIndex] = nextNum
        for i in range(1, len(h_min) + 1):
            nums[changedIndex + i] = heapq.heappop(h_min)
        print(nums)

    def isMax(self, nums):
        for i in range(len(nums)-1):
            if nums[i] < nums[i + 1]:
                return False
        return True

    def run(self):
        # print(self.nextPermutation([1, 2, 3]))
        print(self.nextPermutation([3, 2, 1]))
        # print(self.nextPermutation([1, 1, 5]))

foo = Solution()
foo.run()
