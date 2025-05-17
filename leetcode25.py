# Same tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True  # Both nodes are None
        if not p or not q:
            return False  # One of the nodes is None
        if p.val != q.val:
            return False  # Node values are different
        
        # Recursively check left and right children
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
