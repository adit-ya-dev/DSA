"Given an integer n, break it into at least two positive integers
to maximize the product.
🔹 Example
Input: 10
Output: 36
Explanation: 3 × 3 × 4 = 36
"

def integerBreak(n):
    if n <= 3:
        return n - 1

    result = 1
    while n > 4:
        result *= 3
        n -= 3

    return result * n
