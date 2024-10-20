class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}

        for i in nums:
            if i in hashtable:
                return True
            else:
                hashtable[i] = 0

        return False