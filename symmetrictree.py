# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def res1(root,result1):
            if root!=None:
                result1.append(root.val)
                if root.left:
                    res1(root.left,result1)
                else:
                    result1.append(1000)
                                
                if root.right:
                    res1(root.right,result1)
                else:
                    result1.append(2000)
        def res2(root,result2):
            if root!=None:
                result2.append(root.val)
                if root.right:
                    res2(root.right,result2)
                else:
                    result2.append(1000)
                
                if root.left:
                    res2(root.left,result2)
                else:
                    result2.append(2000)
                
        result1=[]
        result2=[]
        res1(root.left,result1)
        res2(root.right,result2)
        if(result1==result2):
            print(result1,result2)
            return True
        else:
            print(result1,result2)
            return False
