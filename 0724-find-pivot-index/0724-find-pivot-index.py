class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        self.nums = nums
        leftSum = 0
        rightSum = sum(nums) 
        for i in range(len(nums)):
            if(leftSum == rightSum - nums[i]):
                return i
            else:
                rightSum -= nums[i]
                leftSum += nums[i]

        return -1
