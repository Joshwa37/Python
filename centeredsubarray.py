class Solution(object):
    def centeredSubarrays(self, nums):
        idx=2
        l=0
        m=l+idx
        out=len(nums)
        suhe=sum(nums[l:m])
        while(idx<=len(nums)):
            while(m<=len(nums)):
                if(l==0):
                    tot=suhe
                else:
                    tot=tot-nums[l-1]
                    tot+=nums[m-1]
                if(tot in nums[l:m]):
                    out+=1
                m+=1
                l+=1
            idx+=1
            l=0
            m=l+idx
            suhe=sum(nums[l:m])
        return out
        

        