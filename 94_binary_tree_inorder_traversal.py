# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        stack = []
        node = root

        while True:
            if node is not None:
                stack.append(node)
                node = node.left
            else:
                if not stack:
                    break

                node = stack.pop()

                inorder.append(node.val)

                node = node.right
        return inorder

        # result = []
        # def inOrder(node):
        #     if node is not None:
        #         inOrder(node.left)
        #         result.append(node.val)
        #         inOrder(node.right)
        # inOrder(root)
        # return result

        # if not root:
        #     return []

        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)