class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for num in nums:
            str_num = str(num)
            for i in range(len(str_num)):
                digit_sum += int(str_num[i])

        # for num in nums:
        #     while num > 0:
        #         digit_sum += num%10
        #         num //= 10

        diff = abs(element_sum - digit_sum)
        return diff