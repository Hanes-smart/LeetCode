
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        nums= sorted(strs)
        num = nums[0]
        count = ""
        for i in range(len(num)):
            if num is None:
                return count
            if len(strs) is 1:
                return strs[0]
            if num[i] == nums[1][i]:
                count+= num[i]
            else:
                break
        return count
