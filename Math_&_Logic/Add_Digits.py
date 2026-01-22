"Given an integer num, repeatedly add its digits until the result has only one digit.


 Example:

Input: num = 38 → Output: 2
Because: 3+8=11 → 1+1=2"

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9
