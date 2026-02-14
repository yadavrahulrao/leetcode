#589. N-ary Tree Preorder Traversal
# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            
            result.append(node.val)   # Visit root
            for child in node.children:  # Traverse children
                dfs(child)
        
        dfs(root)
        return result
