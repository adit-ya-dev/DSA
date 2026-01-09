"Return True if any value appears at least twice.

Example
Input: [1,2,3,1]
Output: True "

def containsDuplicate(nums):
    return len(nums) != len(set(nums))
