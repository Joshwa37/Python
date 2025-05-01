class Solution(object):
    def isAcronym(self, words, s):
        if(len(words)!=len(s)):
            return False
        for i in range(0,len(words)):
            word=words[i]
            if(word[0]!=s[i]):
                print(word[0],s[i])
                return False
        return True


        