def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if(nums[j]<nums[minpos]):
                minpos=j
        temp=nums[i]
        nums[i]=nums[minpos]
        nums[minpos]=temp
nums=[5,2,8,6,7,3]
sort(nums)
print(nums)