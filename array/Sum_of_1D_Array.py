"Return running sum where
runningSum[i] = sum(nums[0] to nums[i])

Example
Input: [1,2,3,4]
Output: [1,3,6,10]"

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums
