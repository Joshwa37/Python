class Solution(object):
    def numIdenticalPairs(self, nums):
        count=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if(i!=j):
                    if(nums[i]==nums[j]):
                        count+=1
        return count
        