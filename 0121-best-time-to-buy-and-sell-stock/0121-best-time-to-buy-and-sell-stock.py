#VapsTech | 08/09/2024
#Complexity: O(n)
#Runtime: 680ms | Beats 88%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        minimum = prices[0]
        profit = 0

        #run through list
        for i in range(size):
            if (prices[i] < minimum): #check to find smallest number
                minimum = prices[i]
            if (prices[i] - minimum > profit): #check the difference between each next number and smallest number
                profit = prices[i] - minimum
        
        return profit



        