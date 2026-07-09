class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        ranges = []
        for num in nums:
            num_str = str(num)
            curr_range = int(max(num_str)) - int(min(num_str))
            ranges.append(curr_range)
        max_range = max(ranges)

        total_sum = 0
        for i in range(len(nums)):
            if ranges[i] == max_range:
                total_sum += nums[i]

        return total_sum