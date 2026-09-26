class Solution:
    def palindromePartition(self, s, k):
        n = len(s)

        # cost[i][j] = minimum changes needed to make
        # s[i:j+1] a palindrome
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                cost[i][j] = cost[i + 1][j - 1] + (s[i] != s[j])

        # dp[p][i] = minimum cost to divide s[:i]
        # into exactly p parts
        INF = float("inf")
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(parts, n + 1):
                # Last part is s[j:i]
                for j in range(parts - 1, i):
                    dp[parts][i] = min(
                        dp[parts][i],
                        dp[parts - 1][j] + cost[j][i - 1]
                    )

        return dp[k][n]
