#Reverse Subarray

class Solution:
	def reverseSubArray(self,arr,l,r):
            l = l-1 
            r = r-1
            def rever(arr,l,r):
                if l == r or l-r == 1:
                    return arr
                arr[l], arr[r] = arr[r] , arr[l]
                rever(arr , l=l+1 , r= r-1)
                return arr
                
            return rever(arr,l,r)

obj = Solution()
print(obj.reverseSubArray([17 ,10, 15 ,10, 15, 14 ,15, 11 ,13 ,20 ,16 ,10, 10 ,16 ,17 ,18 ,17],9,12))

		