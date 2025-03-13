import sys
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        n=0
        inx=0
        min=sys.maxint
        while(n<k):
            print("n")
            for i in range(0,len(nums)):
                if(nums[i]<min):
                    min=nums[i]
                    print(min)
                    inx=i
            nums[inx]=min*multiplier
            min=sys.maxint
            n+=1
        return nums
    