# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        self.k = k
        left = 0
        right = len(tinput) - 1
        self.find(left, right, tinput, 1)
        return tinput[:k]
        
    def find(self, left, right, tinput, level):
        if left >= right:
            return
        div = tinput[left]
        p1 = left
        p2 = right
        while p1 < p2:
            while p1 < p2 and tinput[p2] >= div:
                p2 -= 1
            tinput[p1] = tinput[p2]
            while p1 < p2 and tinput[p1] <= div:
                p1 += 1
            tinput[p2] = tinput[p1]
        tinput[p1] = div
        if p1 == self.k-1:
            return
        elif p1 > self.k - 1:
            self.find(left, p1 - 1, tinput, level+1)
        else: # p1 < self.k - 1
            self.find(p1 + 1, right, tinput, level+1)

    def run(self):
        print(self.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 4))

foo = Solution()
foo.run()


                