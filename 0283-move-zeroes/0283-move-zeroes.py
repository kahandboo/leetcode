class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        if(len(nums) == 1 or 0 not in nums): pass
        else:
            while right<len(nums):
                if(nums[right] != 0):
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                right += 1

        