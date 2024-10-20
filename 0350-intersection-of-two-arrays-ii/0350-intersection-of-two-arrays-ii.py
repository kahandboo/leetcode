class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        hashtable = {}
        result = []

        for i in min(nums1,nums2):
            if i not in hashtable:
                hashtable[i] = 1
            else:
                hashtable[i] += 1
        
        for i in max(nums1,nums2):
            if i in hashtable and hashtable[i] != 0:
                result.append(i)
                hashtable[i] -= 1

        return result