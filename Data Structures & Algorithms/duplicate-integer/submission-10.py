class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = set(nums)
        for i in nums:
            if len(nums) != len(list1):
                return True

        return False
solution = Solution()

print(solution.hasDuplicate([1,2,3,3]))
print(solution.hasDuplicate([1,2,3,4]))