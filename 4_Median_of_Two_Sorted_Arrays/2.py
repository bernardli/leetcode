from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        totalLen = len1 + len2
        even = totalLen % 2 == 0
        if even:
            k = int(totalLen / 2)
        else:
            k = totalLen // 2 + 1
        index1, index2 = 0, 0
        result = 0

        while k > 0:
            if len1 == 0:
                result += nums2[index2 + k - 1]
                len2 -= 1
                index2 += 1
                break
            if len2 == 0:
                result += nums1[index1 + k - 1]
                len1 -= 1
                index1 += 1
                break
            if k == 1:
                if nums1[index1] < nums2[index2]:
                    result += nums1[index1]
                    len1 -= 1
                    index1 += 1
                else:
                    result += nums2[index2]
                    len2 -= 1
                    index2 += 1
                break
            center = k // 2 - 1
            point1 = min(center, len1 - 1)
            point2 = min(center, len2 - 1)
            if nums1[index1 + point1] < nums2[index2 + point2]:
                len1 -= point1 + 1
                index1 = index1 + point1 + 1
                k -= point1 + 1
            else:
                len2 -= point2 + 1
                index2 = index2 + point2 + 1
                k -= point2 + 1

        # 如果是偶数，还要再往前找一个
        if even:
            if len1 > 0 and len2 > 0:
                result += min(nums1[index1], nums2[index2])
            elif len1 > 0:
                result += nums1[index1 + k - 1]
            elif len2 > 0:
                result += nums2[index2 + k - 1]
            return float(result / 2)
        else:
            return float(result)

    def run(self):
        print(self.findMedianSortedArrays([1, 3], [2]))
        print(self.findMedianSortedArrays([1, 2], [3, 4]))

        print(self.findMedianSortedArrays(
            [1, 3, 4, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
        print(self.findMedianSortedArrays([], [2, 3]))
        print(self.findMedianSortedArrays([], [1, 2, 3, 4]))
        print(self.findMedianSortedArrays([1], [2, 3]))


foo = Solution()
foo.run()
