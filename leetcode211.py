class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # Result list
        res = []

        # Boundary pointers
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # Continue until boundaries cross
        while top <= bottom and left <= right:

            # 1. Traverse left -> right
            for j in range(left, right + 1):
                res.append(matrix[top][j])

            # top row finished
            top += 1

            # 2. Traverse top -> bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])

            # right column finished
            right -= 1

            # 3. Traverse right -> left
            # Check needed to avoid duplicates
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])

                # bottom row finished
                bottom -= 1

            # 4. Traverse bottom -> top
            # Check needed to avoid duplicates
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])

                # left column finished
                left += 1

        return res


s = Solution()
print(s.spiralOrder([[1,2,3],
                     [4,5,6],
                     [7,8,9]]))