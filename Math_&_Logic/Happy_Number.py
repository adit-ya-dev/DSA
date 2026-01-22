"A number is happy if repeatedly replacing it with the sum of squares of its digits eventually becomes 1.
If it loops forever, it's not happy.


Example:

Input: n = 19 → Output: true
Because: 1²+9² = 82 → 8²+2² = 68 → 6²+8² = 100 → 1²+0²+0² = 1" 

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            s = 0
            while n > 0:
                digit = n % 10
                s += digit * digit
                n //= 10
            n = s

        return True
