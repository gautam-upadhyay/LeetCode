class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        seen = {} #dict()                # Dictionary
        for num in nums:
            if num in seen:
                return True
            seen[num] = True
        return False

        # seen = set()                #Set
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False