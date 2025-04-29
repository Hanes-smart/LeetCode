import string
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        rev = ''.join(reversed(a))
        if rev == a:
            return rev == a
        else:
            return False  
p =  Solution()
print(p.isPalindrome(121))
print(p.isPalindrome(-121))
print(p.isPalindrome(10))


        