class Solution(object):
    def transformArray(self, nums):
        lis=[]
        for i in range(0,len(nums)):
            if(nums[i]%2==0):
                lis.insert(0,0)
            else:
                lis.append(1)
        return lis