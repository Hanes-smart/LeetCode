class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        f,l = 0 ,len(nums)-1

        while f<=l:
            mid = (f + l) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                f = mid + 1
            else:
                l =mid - 1
        
        return f

s = Solution()
print(s.searchInsert([1,3,5,6],5))
print(s.searchInsert([1,3,5,6],2))
print(s.searchInsert([1,3,5,6],7))






