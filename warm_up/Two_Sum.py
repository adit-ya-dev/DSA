"Given an array and a target, return indices of two numbers whose sum is equal to target.

def twoSum(nums, target):
    lookup = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in lookup:
            return [lookup[diff], i]
        lookup[nums[i]] = i
