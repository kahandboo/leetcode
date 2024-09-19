class Solution(object):
    def removeDuplicates(self, nums):
        nonUnique = 0
        unique = 0
        while(nonUnique < len(nums)):
            if (nums[unique] == nums[nonUnique]) and unique != nonUnique:
                del nums[nonUnique]
            elif nums[unique] != nums[nonUnique]:
                unique = nonUnique
            else:
                nonUnique += 1
        return len(nums)


        