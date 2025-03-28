class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count=0
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                for k in range(0,len(nums)):
                    if(i!=j and j!=k and k!=i):
                        if(i<j and j<k):
                            if(nums[j]-nums[i]==diff and nums[k]-nums[j]==diff):
                                count+=1
        return count



        