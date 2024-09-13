class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        sum = 0
        count = 0
        sum_map = {0:1}

        for num in nums:
            sum += num
            if sum-k in sum_map:
                count += sum_map[sum-k]
            if sum in sum_map:
                sum_map[sum] += 1
            else:
                sum_map[sum] = 1

        return count
