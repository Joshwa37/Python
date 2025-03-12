class Solution(object):
    def maximumWealth(self, accounts):
        max=0
        for i in range(0,len(accounts)):
            sum1=sum(accounts[i])
            if(max<sum1):
                max=sum1
        return max