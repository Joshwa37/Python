# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def res1(p,result1):
            if p!=None:
                result1.append(p.val)
                if p.left:
                    res1(p.left,result1)
                else:
                    result1.append(10000)
                
                if p.right:
                    res1(p.right,result1)
                else:
                    result1.append(10000)
        def res2(q,result2):
            if q!=None:
                result2.append(q.val)
                if q.left:
                    res2(q.left,result2)
                else:
                    result2.append(10000)
                if q.right:
                    res2(q.right,result2)
                else:
                    result2.append(10000)
        result1=[]
        result2=[]
        res1(p,result1)
        res2(q,result2)
        if(result1==result2):
            print(result2)
            print(result1)
            return True
        else:
            print(result2)
            print(result1)
            return False
