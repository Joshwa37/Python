class Solution(object):
    def maxProfit(self, prices):
        current=prices[0]
        max=0
        for i in range(1,len(prices)):
            if(prices[i]<current):
                current=prices[i]
            else:
                if(max<prices[i]-current):
                    max=prices[i]-current
        return max
