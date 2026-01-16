"Given n, return n!
Example: 5! = 5*4*3*2*1 = 120
"

class Solution:
    def factorial(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
