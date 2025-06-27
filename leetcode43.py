#Count the Number of Inversions



MOD = 10**9 + 7

class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        # Map end index to required inversion count
        req_map = {endi: cnti for endi, cnti in requirements}
        
        max_inv = n * (n - 1) // 2  # Max possible inversions in size n
        dp = [ [0] * (max_inv + 1) for _ in range(n + 1) ]
        dp[0][0] = 1  # 1 way to build empty array with 0 inversions

        for i in range(1, n + 1):  # i is the current length of prefix
            for inv in range(max_inv + 1):
                if dp[i - 1][inv] == 0:
                    continue
                # Insert current number at any position in [0, i-1]
                for pos in range(i):
                    new_inv = inv + (i - 1 - pos)
                    if new_inv <= max_inv:
                        dp[i][new_inv] = (dp[i][new_inv] + dp[i - 1][inv]) % MOD

            # Apply requirement filtering if there's one for this prefix length
            if (i - 1) in req_map:
                required_inv = req_map[i - 1]
                new_dp_row = [0] * (max_inv + 1)
                new_dp_row[required_inv] = dp[i][required_inv]
                dp[i] = new_dp_row

        # The final permutations must satisfy the requirement for n-1
        return sum(dp[n]) % MOD
