class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n:
            return -1

        ans = 0
        for _ in range(n):
            curr_digit = min(9, s)
            ans = ans * 10 + curr_digit
            s -= curr_digit

        return ans