class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        res = 0
        left = 0
        for right in range(0,len(s)):
            while s[right] in d:
                d.remove(s[left])
                left +=1

            d.add(s[right])
            res =  max(res,right-left+1)
            
        return res




        