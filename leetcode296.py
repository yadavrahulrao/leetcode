#1123. Lowest Common Ancestor of Deepest Leaves

class Solution:
    def lcaDeepestLeaves(self, root):
        def dfs(node):
            if not node:
                return 0, None

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth == right_depth:
                return left_depth + 1, node

            if left_depth > right_depth:
                return left_depth + 1, left_lca

            return right_depth + 1, right_lca

        return dfs(root)[1]
