class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        out=[]
        count=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(nums[i]>nums[j]):
                    count+=1
            out.append(count)
            count=0
        return out
        