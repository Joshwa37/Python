class Solution(object):
    def countConsistentStrings(self, allowed, words):
        sor="".join(sorted(allowed))
        count=0
        chec=0
        for i in range(0,len(words)):
            sorted_s = "".join(sorted(words[i]))
            lis=list(set(sorted_s))
            let="".join(lis)
            if(len(let)>len(sor)):
                continue
            elif(len(let)<=len(sor)):
                for i in let:
                    if i in sor:
                        chec+=1
                if(chec==len(let)):
                    count+=1
                    print(let)
                chec=0
        return count
        