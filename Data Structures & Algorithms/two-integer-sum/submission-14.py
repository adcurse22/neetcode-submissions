class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for o in range(len(nums)):
                if i != o and nums[i] + nums[o] == target:
                    return [i,o]
                