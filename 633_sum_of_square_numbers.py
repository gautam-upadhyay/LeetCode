class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)

        while left <= right:
            if left*left + right*right == c:
                return True
            elif left*left + right*right < c:
                left += 1
            else:
                right -= 1
        return False

        # a = 0
        # b = int(c**0.5)

        # while a <= b:
        #     curr_sum = a**2 + b**2

        #     if curr_sum == c:
        #         return True
        #     elif curr_sum < c:
        #         a += 1
        #     else:
        #         b -= 1
        # return False