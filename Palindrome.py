class Solution:
    def isPalindrome(x):
        num=x
        rem=0
        rev=0
        if(x<0):
            return False
        while(num>0):
            rem=num%10
            num=num//10
            rev=rev*10+rem
        if(rev==x):
            return True
        else:
            return False

print(Solution.isPalindrome(121))


