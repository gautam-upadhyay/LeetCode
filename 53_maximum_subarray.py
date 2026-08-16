class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for num in nums:
            currSum = max(num, num + currSum)
            maxSum = max(maxSum, currSum)

        return maxSum