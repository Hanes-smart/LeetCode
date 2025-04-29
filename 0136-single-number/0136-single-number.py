class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count =0
        if len(nums)== 1:
            return nums[0]
        for i in range(len(nums)):
            count = count^nums[i]
        return count

S= Solution()
print(S.singleNumber([2,2,1]))
print(S.singleNumber([4,1,2,1,2]))

        