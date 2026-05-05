class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def solve(k):
            if k == 1:
                return 1
            if k == 2:
                return 2

            if k in cache:
                return cache[k]

            cache[k] = solve(k-1) + solve(k-2)
            return cache[k]

        return solve(n)