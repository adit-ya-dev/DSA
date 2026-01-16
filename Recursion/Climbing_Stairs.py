"Problem

You are climbing stairs. You can take 1 step or 2 steps.
Return how many distinct ways to reach the top.

Example:
n=3 → 3 ways
1+1+1
1+2
2+1"

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def solve(x):
            if x == 0:
                return 1
            if x < 0:
                return 0
            if x in memo:
                return memo[x]

            memo[x] = solve(x - 1) + solve(x - 2)
            return memo[x]

        return solve(n)
