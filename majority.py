nums=[]
check=0
num=0
n=len(nums)//2
nu=0
for i in range(0,len(nums)):
    count=0
    if(nu==nums[i]):
        continue
    for j in range(0,len(nums)):
        if(nums[i]==nums[j]):
            count=count+1
            if(count>n):
                nu=nums[j]
                break
    if(count>check):
        check=count
        num=nums[i]
    if(check>n):
        print(num) 
        break
print(num)