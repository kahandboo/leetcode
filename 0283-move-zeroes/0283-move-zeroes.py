class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == 0:
                del nums[i]
                count += 1
            i -= 1

        while count > 0:
            nums.append(0)
            count -= 1

    

        