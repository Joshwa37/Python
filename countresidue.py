class Solution(object):
    def residuePrefixes(self, s):
        out=0
        for i in range(0,len(s)):
            if(len(s[:i+1])%3==len(list(set(s[:i+1])))):
                out+=1
        return out
        
        