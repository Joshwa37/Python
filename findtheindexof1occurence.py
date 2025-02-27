class Solution(object):
    def strStr(self, haystack, needle):
        check=len(needle)
        if(len(needle)>len(haystack)):
            return -1
        for i in range(0,len(haystack)):
            if(haystack[i:check+i]==needle):
                return i
        return -1