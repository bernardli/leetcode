from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapestBuy = -float('inf')
        profit = 0
        for price in prices:
            cheapestBuy = max(-price, cheapestBuy)
            profit = max(profit, price + cheapestBuy)

        return profit

    def run(self):
        print(self.maxProfit([7, 1, 5, 3, 6, 4]))
        print(self.maxProfit([7, 6, 4, 3, 1]))


foo = Solution()
foo.run()
