import copy
class Solution(object):
    def setZeroes(self, matrix):
        mat=[]
        mat2=copy.deepcopy(matrix)
        for i in matrix[0]:
            mat.append(0)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(mat2[i][j]==0):
                    matrix[i]=mat
                    for k in range(0,len(matrix)):
                        matrix[k][j]=0
                        print(k,j)
        return matrix
                    
                
        