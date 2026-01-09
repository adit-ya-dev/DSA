"Given a sorted array, remove the duplicates in-place such that each element appears only once.
Return the number of unique elements k.

🔸 You must modify the array in-place.

Example
Input: nums = [1,1,2]
Output: k = 2, nums = [1,2,_] "

def removeDuplicates(nums):
    if not nums:
        return 0

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
