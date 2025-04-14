class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        l=0
        m=0
        count=0
        while(l<len(arr)):
            if(l==0):
                count+=sum(arr)
                l+=2
                print("hi",l,m,count)
            elif(l>0 and l<len(arr)-1):
                if(m+l<len(arr)):
                    if(m+l==len(arr)-1):
                        count+=sum(arr[m:m+l+1])
                        l+=2
                        m=0
                        print("hi1",l,m,count)  
                    else:
                        count+=sum(arr[m:m+l+1])
                        m+=1
                        print("hi2",l,m,count)
                    
            elif(l==len(arr)-1):
                count+=sum(arr)
                l+=2
                print("hi3",l,m,count)
            
        return count


                
        