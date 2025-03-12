class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ma=max(candies)
        lis=[]
        for i in candies:
            if(i+extraCandies>=ma):
                lis.append(True)
            else:
                lis.append(False)
        return lis