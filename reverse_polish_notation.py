import math
class Solution(object):
    def evalRPN(self, tokens):
        tot=0
        lis=[]
        for i in tokens:
            if i in {"+", "-", "*", "/"}:
                b = lis.pop()
                a = lis.pop()
            if i== "+":
                tot+=a+b
                lis.append(tot)
                tot=0
            elif i=="-":
                tot+=a-b
                lis.append(tot)
                tot=0
            elif i=="*":
                tot+=a*b
                lis.append(tot)
                tot=0
            elif i=="/":
                if(a==0 or b==0):
                    lis.append(0)
                    continue
                lis.append(int(float(a) / b)) 
                tot=0
            else:
                lis.append(int(i))
        return lis[0]
        
                
        