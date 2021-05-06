from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyProfit_1 = -prices[0]
        sellProfit_1 = 0
        buyProfit_2 = -prices[0]
        sellProfit_2 = 0
        for i in range(1, len(prices)):
            buyProfit_1 = max(-prices[i], buyProfit_1)
            sellProfit_1 = max(prices[i] + buyProfit_1, sellProfit_1)
            buyProfit_2 = max(-prices[i] + sellProfit_1, buyProfit_2)
            sellProfit_2 = max(prices[i] + buyProfit_2, sellProfit_2)

        return max(sellProfit_2, 0)

    def run(self):
        print(self.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))
        print(self.maxProfit([1, 2, 3, 4, 5]))
        print(self.maxProfit([7, 6, 4, 3, 1]))
        print(self.maxProfit([1]))


foo = Solution()
foo.run()
