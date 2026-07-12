class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        res = k

        MOD = 10**9+7
        avail = k
        total = 0

        for num in nums:
            if avail < num:
                diff = num - avail
                needed_ops, remain = divmod(diff, k)

                if(remain > 0):
                    needed_ops += 1

                total += needed_ops

                avail += needed_ops * k
            avail -= num
        total= (total *(total+1)) // 2
        return total % MOD