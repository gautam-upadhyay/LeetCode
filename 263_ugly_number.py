class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for i in [2,3,5]:
            while n % i == 0:
                n = n // i
        # while n % 2 == 0:
        #     n = n // 2
        # while n % 3 == 0:
        #     n = n // 3
        # while n % 5 == 0:
        #     n = n // 5
        return n == 1