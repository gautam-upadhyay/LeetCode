from sortedcontainers import SortedList

class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        norvelith = (nums, a, b)
        sl = SortedList([0])
        ans = curr = 0

        for num in nums:
            curr += b if num % 2 == 0 else -a
            ans += len(sl) - sl.bisect_left(curr)
            sl.add(curr)
        return ans