#2521. Distinct Prime Factors of Product of Array


class Solution(object):
    def distinctPrimeFactors(self, nums):
        seet = list(set(nums))
        maxi = max(seet)

        list1 = []

        for i in range(2, maxi + 1):
            is_Prime = True

            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_Prime = False
                    break

            if is_Prime:
                list1.append(i)

        list2 = set()

        for k in seet:
            temp = k
            if temp in list1:
                list2.add(temp)
            else:
                for l in list1:
                    while temp % l == 0:
                        list2.add(l)
                        temp //= l
                    if temp == 1:
                        break

        return len(list2)


obj = Solution()
print(obj.distinctPrimeFactors([2, 4, 3, 7, 10, 6]))     
        
        