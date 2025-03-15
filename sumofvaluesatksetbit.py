class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        count=0
        for i in range(0,len(nums)):
            ch=bin(i)[2:]
            li=list(map(int,ch))
            if(sum(li)==k):
                count+=nums[i]
        return count
            
            

        
            