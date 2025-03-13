class Solution(object):
    def leftRightDifference(self, nums):
        ltotal=0
        rtotal=sum(nums)-nums[0]
        r=1
        l=0
        q=0
        while(q<len(nums)):
            n=nums[l]
            if(ltotal-rtotal>0):
                print(ltotal,rtotal,ltotal-rtotal)
                nums[q]=ltotal-rtotal
            else:
                print(ltotal,rtotal,ltotal-rtotal)
                nums[q]=(ltotal-rtotal)*-1
            ltotal+=n
            if(r<len(nums)):
                n=nums[r]
                rtotal-=n
            l+=1
            r+=1
            q+=1
        return nums



        