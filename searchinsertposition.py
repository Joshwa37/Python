class Solution(object):
    def searchInsert(self, nums, target):
        if(nums[0]>=target):
            return 0
        for i in range(0,len(nums)-1):
            if(target==nums[i]):
                return i
            else:
                if(nums[i]<target and nums[i+1]>target):
                    return i+1
        if(nums[len(nums)-1]==target):
            return len(nums)-1
        else:
            return len(nums)