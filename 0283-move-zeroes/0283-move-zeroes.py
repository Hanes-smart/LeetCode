class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num 
                insert_pos +=1

        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos +=1
            
s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
    