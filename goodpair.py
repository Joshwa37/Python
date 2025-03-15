class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        count=0
        
        for i in range(0,len(nums1)):
            for j in range(0,len(nums2)):
                if(nums1[i]%(nums2[j]*k)==0):
                    print(nums1[i],nums2[j])
                    count+=1
        return count        