class Solution(object):
    def findMatrix(self, nums):
        count=0
        out=[]
        for i in range(0,len(nums)):
            for j in range(0,len(out)):
                if(nums[i] in out[j]):
                    count+=1
                else:
                    break
            if(count==0 and len(out)==0):
                out.append([nums[i]])
            elif(count==0):
                out[count].append(nums[i])
            elif(count==len(out)):
                out.append([nums[i]])
            else:
                out[count].append(nums[i])
            count=0
        return out


        