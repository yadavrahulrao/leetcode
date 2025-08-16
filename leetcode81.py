# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # This will hold the maximum diameter found

        def dfs(node):
            if not node:
                return 0  # Height of a null node is 0

            # Recursively find the height of the left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update the diameter at this node
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            # Return height of the tree rooted at this node
            return 1 + max(left_height, right_height)

        dfs(root)
        return self.max_diameter
