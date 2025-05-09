class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in range(len(s)):
            if 48 <= ord(s[i]) <= 57 or 97 <= ord(s[i]) <= 122:
                res += s[i]
            elif 65 <= ord(s[i]) <= 90:
                res += s[i].lower()
        return res == res[::-1]


