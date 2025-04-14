class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        out=[]
        res=[]
        for i in grid:
            out+=i
        print(out)

        for i in range(1,max(out)+2):
            if(i in out):
                continue
            else:
                res.append(i)
                break
        out.sort()
        for i in range(0,len(out)-1):
            if(out[i]==out[i+1]):
                res.insert(0,out[i])
                break
        return res

        