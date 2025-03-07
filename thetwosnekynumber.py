class Solution(object):
    def getSneakyNumbers(self, nums):
        a=[]
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if(i!=j):
                    if(nums[i]==nums[j]):
                        a.append(nums[i])
        a=list(set(a))
        return a

        