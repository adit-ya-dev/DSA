"Given an array nums, return the element that appears more than n/2 times.

Example:

nums = [3,2,3] → Output: 3"

class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
