Python
class Solution(object):
    def maximumTripletValue(self, nums):
        max=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    val=(nums[i] - nums[j]) * nums[k]
                    if(max<val):
                        max=val
        return maxadd