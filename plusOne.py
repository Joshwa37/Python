class Solution:
    def plusOne(digits):
        sum=0
        list=[]
        for i in digits:
            sum=sum*10+i
        sum=sum+1
        while(sum>0):
            rem=sum%10
            list.append(rem)
            sum=sum//10
        list.reverse()
        return list
print(Solution.plusOne([1,2,3]))