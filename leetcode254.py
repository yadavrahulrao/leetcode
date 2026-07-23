#1588. Sum of All Odd Length Subarrays

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        sums = sum(arr)
        n = len(arr)
        res = []
        if n < 3 :
            return sums
        elif n >= 3 :
            for i in range(1,n+1,2):
                for j in range(n-i+1):
                    res.append(arr[j:j+i])
            sing = [k for l in res for k in l]
            sumss = sum(sing)
            return sumss   
    
obj = Solution()
print(obj.sumOddLengthSubarrays([1,4,2,5,3]))
        