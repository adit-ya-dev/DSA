"An array is called balance-nice if:"
"(sum of even indices) − (sum of odd indices) = 0
"Given an array, return the number of ways to remove exactly one element such that the remaining array is balance-nice.

"Example
Input: nums = [3, 1, 2, 4]
Even indices → 3 + 2 = 5
Odd indices  → 1 + 4 = 5
Output: 0
"

def minOperationsBalanceNice(nums):
    even_sum = 0
    odd_sum = 0

    for i in range(len(nums)):
        if i % 2 == 0:
            even_sum += nums[i]
        else:
            odd_sum += nums[i]

    return abs(even_sum - odd_sum)
