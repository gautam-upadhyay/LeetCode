# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []

        if root is None:
            return preorder
        
        stack = [root]

        while stack:
            node = stack.pop()
            preorder.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return preorder


        # result = []
        # def traversal(node):
        #     if node is not None:
        #         result.append(node.val)
        #         traversal(node.left)
        #         traversal(node.right)

        # traversal(root)
        # return result

        # if not root:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)