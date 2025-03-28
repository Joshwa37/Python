class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        a=len(pref)
        for i in words:
            if(pref==i[0:a]):
                count+=1  
        return count
        