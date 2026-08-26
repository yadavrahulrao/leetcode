#667. Beautiful Arrangement II


class Solution:
    def constructArray(self, n, k):
        ans = []

        l, r = 1, n

        while l <= r:
            if k > 1:
                if k % 2 == 1:
                    ans.append(l)
                    l += 1
                else:
                    ans.append(r)
                    r -= 1

                k -= 1
            else:
                ans.append(l)
                l += 1

        return ans
