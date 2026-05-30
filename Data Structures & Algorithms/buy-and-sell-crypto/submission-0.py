class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        Buy = 0

        max_profit = 0

        for Sell in range(1,len(prices)):

            if prices[Buy] > prices[Sell]:
                Buy = Sell

            else:
                max_profit = max(max_profit,prices[Sell]-prices[Buy])


        return max_profit    
            







        