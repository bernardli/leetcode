from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        waterSum = 0
        left = 0
        right = len(height) - 1

        while left < len(height):
            if height[left] > 0:
                break
            left += 1

        while right >= 0:
            if height[right] > 0:
                break
            right -= 1

        priorHeight = 0
        while left < right:
            currHeight = min(height[left], height[right])
            pointer = left + 1
            blockVolumeSum = 0
            while pointer < right:
                if height[pointer] < currHeight:
                    blockVolumeSum += max(0, height[pointer] - priorHeight)
                else:
                    blockVolumeSum += currHeight - priorHeight
                pointer += 1

            waterSum += (right - left - 1) * \
                (currHeight - priorHeight) - blockVolumeSum
            priorHeight = currHeight
            print(waterSum)

            if height[left] < height[right]:
                pointer = left + 1
                while pointer < right:
                    if height[pointer] > height[left]:
                        break
                    pointer += 1
                left = pointer
            elif height[left] > height[right]:
                pointer = right - 1
                while left < pointer:
                    if height[pointer] > height[right]:
                        break
                    pointer -= 1
                right = pointer
            else:
                pointer1 = left + 1
                while pointer1 < right:
                    if height[pointer1] > height[left]:
                        break
                    pointer1 += 1
                pointer2 = right - 1
                while left < pointer2:
                    if height[pointer2] > height[right]:
                        break
                    pointer2 -= 1
                left = pointer1
                right = pointer2

        # currHeight = 1
        # while left < right:
        #     if height[left] >= currHeight and height[right] >= currHeight:
        #         pointer = left + 1
        #         priorPosition = left
        #         while pointer <= right:
        #             if height[pointer] >= currHeight:
        #                 waterSum += pointer - priorPosition - 1
        #                 priorPosition = pointer
        #             pointer += 1
        #         print(waterSum)
        #         currHeight += 1
        #     elif height[left] < currHeight:
        #         left += 1
        #         while left < right:
        #             if height[left] >= currHeight:
        #                 break
        #             left += 1
        #     elif height[right] < currHeight:
        #         right -= 1
        #         while right > left:
        #             if height[right] >= currHeight:
        #                 break
        #             right -= 1

        return waterSum

    def run(self):
        # print(self.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        # print(self.trap([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5,
        #                  3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]))
        print(self.trap([3, 9, 2, 2, 8, 8, 7, 3]))


foo = Solution()
foo.run()
