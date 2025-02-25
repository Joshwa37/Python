class Solution(object):
    def moveZeroes(self, nums):
        zeros=len(nums)-1
        i=0
        while i<len(nums):
            if(i==zeros):
                break
            else:
                if(nums[i]==0):
                    nums.remove(0)
                    zeros-=1
                    nums.append(0)
                else:
                    i+=1
        return nums