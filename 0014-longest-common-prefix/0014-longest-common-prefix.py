class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        nums = min(len(s) for s in strs)
        num = strs[0][:nums] 
        for i in range(1,len(strs)):
            count = ""
            for j in range(len(num)):
                if strs[i][j] == num[j]:
                    count+=  num[j]
                else:
                    break
            num =count
        return num

S= Solution()
print(S.longestCommonPrefix(["flower","flow","flight"]))