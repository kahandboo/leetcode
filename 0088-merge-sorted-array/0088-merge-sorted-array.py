class Solution(object):
    def merge(self, nums1, m, nums2, n):
        j = 0
        for i in range(m,m+n):
            nums1[i] = nums2[j]
            j += 1
        
        nums1[:m+n] = sorted(nums1[:m+n])
        return nums1[:m+n]
        