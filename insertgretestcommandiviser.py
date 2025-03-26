# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        itr=head
        while(itr.next):
            n=itr.val
            m=itr.next.val
            if(m>n):
                n,m=m,n
            while m != 0:
                n, m = m, n % m
            node=ListNode(n,itr.next)
            itr.next=node
            itr=itr.next.next
        return head