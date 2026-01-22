"Given two non-negative integers low and high, return the count of odd numbers between them (inclusive).



 Example:

Input: low = 3, high = 7 → Output: 3
Odds are: 3, 5, 7"

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = high - low + 1
        if low % 2 == 1 or high % 2 == 1:
            return (total + 1) // 2
        return total // 2
