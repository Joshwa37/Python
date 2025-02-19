class Solution(object):
    def romanToInt(self, s):
        lis=list(s)
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        nums=0
        i=len(lis)-1
        while(i>=0):
            if(i!=0):
                if(dict.get(lis[i])>dict.get(lis[i-1])):
                    nums=nums+(dict.get(lis[i])-dict.get(lis[i-1]))
                    print(nums)
                    if(i==1):
                        return nums
                    i=i-1
                else:
                    nums=nums+dict.get(lis[i])
                    print(nums)
            else:
                nums=nums+dict.get(lis[i])
            i=i-1
        return nums