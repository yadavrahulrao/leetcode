#2916. Subarrays Distinct Element Sum of Squares II

class Solution(object):
    def sumCounts(self, nums):
        mod = 10 ** 9 +7
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = set()
            res = 0
            for j in range(i,n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    res += 1
                ans = (ans + res * res) % mod
        return ans
       
        

# class Solution(object):
#     def sumCounts(self, nums):
#         MOD = 10**9 + 7
#         n = len(nums)

#         total = [0] * (4 * n)
#         squares = [0] * (4 * n)
#         lazy = [0] * (4 * n)

#         def update(node, left, right, ql, qr):
#             if ql > right or qr < left:
#                 return

#             if ql <= left and right <= qr:
#                 length = right - left + 1
#                 v = lazy[node] + 1
#                 squares[node] = (
#                     squares[node] + 2 * total[node] + length
#                 ) % MOD
#                 total[node] = (total[node] + length) % MOD
#                 lazy[node] = v
#                 return

#             mid = (left + right) // 2
#             lc = node * 2
#             rc = lc + 1

#             if lazy[node]:
#                 v = lazy[node]
#                 for child, l, r in (
#                     (lc, left, mid),
#                     (rc, mid + 1, right)
#                 ):
#                     length = r - l + 1
#                     squares[child] = (
#                         squares[child] + 2 * v * total[child]
#                         + v * v * length
#                     ) % MOD
#                     total[child] = (
#                         total[child] + v * length
#                     ) % MOD
#                     lazy[child] += v
#                 lazy[node] = 0

#             update(lc, left, mid, ql, qr)
#             update(rc, mid + 1, right, ql, qr)

#             total[node] = (total[lc] + total[rc]) % MOD
#             squares[node] = (
#                 squares[lc] + squares[rc]
#             ) % MOD

#         last = {}
#         ans = 0

#         for r, x in enumerate(nums):
#             start = last.get(x, -1) + 1
#             update(1, 0, n - 1, start, r)
#             last[x] = r
#             ans = (ans + squares[1]) % MOD

#         return ans
