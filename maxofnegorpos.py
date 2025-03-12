class Solution(object):
    def maximumCount(self, nums):
        neg=0
        pos=0
        for i in nums:
            if(i==0):
                continue
            elif(i<0):
                neg+=1
            elif(i>0):
                pos+=1
        print("udgjh")
        if(neg>pos):
            return neg
        else:
            return pos
        