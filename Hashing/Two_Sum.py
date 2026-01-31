"Given an array nums and an integer target, return indices of the two numbers such that they add up to target.

Example:
nums = [2,7,11,15], target = 9 → Output: [0,1]"

class Solution:
    def twoSum(self, nums, target):
        mp = {}  # value -> index

        for i, num in enumerate(nums):
            need = target - num
            if need in mp:
                return [mp[need], i]
            mp[num] = i
