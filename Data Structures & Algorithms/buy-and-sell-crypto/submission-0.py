class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        for i in range(len(prices)-1):
            profit=0
            for j in range(i+1,len(prices)):
                profit=max(profit,prices[j]-prices[i])
            maxprofit=max(maxprofit,profit)
        return maxprofit

        