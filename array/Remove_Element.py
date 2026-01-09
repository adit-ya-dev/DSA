"Remove all occurrences of val in-place and return the new length.

Example
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_ ,_]"

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
