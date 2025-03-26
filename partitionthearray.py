class Solution(object):
    def pivotArray(self, nums, pivot):
        list1=[]
        list2=[]
        list3=[]
        for i in range(0,len(nums)):
            if(nums[i]==pivot):
                list2.append(nums[i])
            elif(nums[i]>pivot):
                list3.append(nums[i])
            else:
                list1.append(nums[i])
        return list1+list2+list3