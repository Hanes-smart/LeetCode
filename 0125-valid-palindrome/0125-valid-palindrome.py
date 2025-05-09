import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        res =""
        cleaned_text = re.sub(r'[^A-Za-z0-9]', '', s)
        lower = cleaned_text.lower()
        if lower == lower[::-1] :
            return True
        else:
            return False

