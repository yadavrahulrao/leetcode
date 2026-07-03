#204. Count Primes

# class Solution(object):
#     def countPrimes(self, n):
#         res = []
#         for i in range(2,n):
#             for j in range(2,int(i ** 0.5)+1):
#                 if i % j == 0:
#                     break
#             else:
                    
#                 res.append(i)
#         return len(res)
# obj = Solution()
# print(obj.countPrimes(10))
                
                
class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        p = 2
        while p * p < n:
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        return sum(prime)


obj = Solution()
print(obj.countPrimes(10))
        
        
