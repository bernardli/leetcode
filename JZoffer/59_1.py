from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        window = []
        result = []

        if len(nums) == 0:
            return []

        for i in range(k):
            window.append(nums[i])
            if len(queue) == 0:
                queue.append(nums[i])
                continue
            while len(queue) > 0 and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        result.append(queue[0])

        idx = k
        while idx < len(nums):
            removedNum = window.pop(0)
            if removedNum == queue[0]:
                queue.pop(0)
            window.append(nums[idx])
            # if len(queue) == 0:
            #     queue.append(nums[idx])
            #     idx += 1
            #     result.append(queue[0])
            #     continue
            while len(queue) > 0 and nums[idx] > queue[-1]:
                queue.pop()
            queue.append(nums[idx])
            result.append(queue[0])
            idx += 1
            

        return result

    def run(self):
        print(self.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
        print(self.maxSlidingWindow([3, 1, 1, -1, 1], 3))

        print(self.maxSlidingWindow([1, -1], 1))


foo = Solution()
foo.run()
