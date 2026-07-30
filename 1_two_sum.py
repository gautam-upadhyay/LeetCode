class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            require = target - nums[i]

            if require in d:
                return (d[require], i)

            d[nums[i]] = i

        return []

## can't do two pointer as it take o(nlogn)
        # nums.sort()
        # left = 0
        # right = len(nums) - 1

        # while left < right:
        #     total = nums[left] + nums[right]
        #     if total == target:
        #         return [left , right]
        #     elif total < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return []