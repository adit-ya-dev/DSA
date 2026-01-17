"Return an array of unique elements that appear in both arrays.

Example:

nums1 = [1,2,2,1], nums2 = [2,2] → Output: [2]"

class Solution:
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
