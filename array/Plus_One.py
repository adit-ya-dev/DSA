"Given digits representing a number, add 1 and return the result.

Example
Input: [9,9]
Output: [1,0,0] "

def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits
