#Number of factors
class Solution:
    def countFactors (self, n):
        # code here
        # list1 = []
        # for i in range(1,n+1):
        #     if n//i == n/i :
        #         list1.append(i)

        # return len(list1)

        count = 0 
        for i in range(1,int(n**0.5)+1):
            if n % i == 0 :
                if i * i == n :
                    count += 1
                else :
                    count += 2

        return count
