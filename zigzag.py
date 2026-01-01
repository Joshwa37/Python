class Solution(object):
    def convert(self, s, numRows):
        lis=[]
        for i in range(numRows):
            lis.append("")
        idx=0
        flag=0
        if(numRows==1):
            return s
        for i in s:
            lis[idx]+=i
            if(flag==0):
                idx+=1
            else:
                idx-=1
            if(idx>numRows-1):
                flag=1
                idx-=2
            if(idx<0):
                idx+=2
                flag=0
        out=""
        for i in lis:
            out+=i
        return out
            
        





        
        