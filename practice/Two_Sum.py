"Return indices of 2 numbers such that they add up to target."

def twoSum(nums, target):
    mp = {}  # value -> index
    for i, num in enumerate(nums):
        need = target - num
        if need in mp:
            return [mp[need], i]
        mp[num] = i
