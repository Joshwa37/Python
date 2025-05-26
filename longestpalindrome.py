class Solution(object):
    def longestPalindrome(self, s):
        st=""
        max=0
        st=""
        le=0
        out=""
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                if(i!=j):
                    st=s[i:j]
                    if(st==st[::-1]):
                        le=len(st)
                        if(le>max):
                            max=le
                            out=st
                    
        if(out==""):
            return s
        else:
            return out