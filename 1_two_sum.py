class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):               #T.C O(n^2)
        #         if (nums[i] + nums[j] == target):         #S.C O(1)
        #             return [i,j]
        

        map = {}

        for i in range(len(nums)):
            require = target - nums[i]
            if require in map:
                return [map[require], i]

            map[nums[i]] = i

        return []