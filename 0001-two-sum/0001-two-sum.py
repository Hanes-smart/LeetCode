class Solution:
    def twoSum(self, nums, target):
        num_dic = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dic:
                return [num_dic[complement], i]
            num_dic[num] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 2, 4], 6))
print(s.twoSum([3, 3], 6))
print(s.twoSum([2, 5, 5, 11], 10))