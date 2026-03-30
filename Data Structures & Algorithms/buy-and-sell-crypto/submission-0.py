class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        for i in range(len(prices)):
            for j in range(i ,len(prices)):
                    res.append(prices[j] - prices[i])
        return max(res)
                    
        