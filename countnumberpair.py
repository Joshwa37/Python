class Solution(object):
    def countKDifference(self, nums, k):
        count=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if(i<j):
                    if(abs(nums[i]-nums[j])==k):
                        count+=1
        return count


        