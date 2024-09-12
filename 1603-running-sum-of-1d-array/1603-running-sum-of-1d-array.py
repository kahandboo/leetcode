class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        self.nums = nums
        output = []
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            output.append(sums)
        return output
        