class Solution(object):
    def findWordsContaining(self, words, x):
        li=[]
        for i in range(0,len(words)):
            word=words[i]
            for j in range(0,len(word)):
                if(word[j]==x):
                    li.append(i)
                    break
                
        return li