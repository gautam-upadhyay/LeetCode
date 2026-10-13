# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        level_sums = {}

        def dfs(node, level):
            if not node:
                return

            level_sums[level] = level_sums.get(level, 0) + node.val

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 1)

        max_sum = float('-inf')
        min_level = 1

        for level in sorted(level_sums.keys()):
            if level_sums[level] > max_sum:
                max_sum = level_sums[level]
                min_level = level

        return min_level