class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(curr_sum, max_sum)

        return max_sum























        # max_sum = nums[0]
        # curr_sum = 0

        # for num in nums:
        #     curr_sum = max(num, curr_sum + num)
        #     max_sum = max(curr_sum, max_sum)
        # return max_sum

        # max_sum = nums[0]
        # curr_sum = nums[0]

        # for num in nums[1:]:
        #     curr_sum = max(num, curr_sum + num)
        #     max_sum = max(curr_sum, max_sum)
        # return max_sum


        # max_sum = nums[0]
        # curr_sum = 0

        # for i in range(len(nums)):
        #     curr_sum += nums[i]
        #     if curr_sum > max_sum:
        #         max_sum = curr_sum
        #     if curr_sum < 0:
        #         curr_sum = 0

        # return max_sum