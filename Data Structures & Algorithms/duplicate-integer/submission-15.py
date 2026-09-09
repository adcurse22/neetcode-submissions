class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = set(nums)
        return len(nums) != len(list1)
            
solution = Solution()

print(solution.hasDuplicate([1,2,3,3]))
print(solution.hasDuplicate([1,2,3,4]))