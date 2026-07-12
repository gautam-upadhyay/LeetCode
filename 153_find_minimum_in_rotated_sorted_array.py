class Solution:
    def findMin(self, nums: List[int]) -> int:
        # min = nums[0]
        # for i in range(len(nums)):
        #     if nums[i] < min:
        #         min = nums[i]

        # return min  #O(n)
       
        # return min(nums) #O(n)

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right -  left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]  #O(logn)