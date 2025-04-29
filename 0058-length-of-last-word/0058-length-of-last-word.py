class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        b = a.pop()
        return len(b)

S= Solution()
S.lengthOfLastWord("Hello World")
S.lengthOfLastWord("   fly me   to   the moon  ")
S.lengthOfLastWord("luffy is still joyboy")