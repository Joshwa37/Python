class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums=nums1+nums2
        nums.sort()
        n=0
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return nums[0]
        elif(len(nums)%2==0):
            n=len(nums)//2
            print(nums[n-1],nums[n])
            if((nums[n-1]+nums[n])%2==0):
                return (nums[n-1]+nums[n])//2
            else:
                return (nums[n-1]+nums[n])//2+0.5
        elif(len(nums)%2==1):
            n=(len(nums)+1)/2
            return nums[n-1]
        
        

        
        