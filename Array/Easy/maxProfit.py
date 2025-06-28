class Solution(object):
    def maxProfit(self, prices):
        profite = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profite = profite + prices[i] - prices[i-1]
        return profite
    
prices = [7,1,5,3,6,4]
sol = Solution()
k = sol.maxProfit(prices)
print(k)  # Output: 7