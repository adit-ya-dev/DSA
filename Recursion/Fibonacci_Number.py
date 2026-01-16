"Given n, return the n-th Fibonacci number.
Fibonacci: F(0)=0, F(1)=1, and F(n)=F(n-1)+F(n-2)."

class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def solve(x):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x in memo:
                return memo[x]

            memo[x] = solve(x - 1) + solve(x - 2)
            return memo[x]

        return solve(n)
