#133. Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node:'Node') -> 'Node':
      otn = {}
      def dfs(node):
        if node in otn :
          return otn[node]
        copy = Node(node.val)
        otn[node] = copy
        for neighbor in node.neighbors:
          copy.neighbors.append(dfs(neighbor))
        return copy
      return dfs(node) if node else None