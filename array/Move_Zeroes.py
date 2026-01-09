"Move all zeros to the end, keeping order of non-zero elements.

Example
Input: [0,1,0,3,12]
Output: [1,3,12,0,0] "

def moveZeroes(nums):
    k = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
