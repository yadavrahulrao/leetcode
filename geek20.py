#Largest in Array




class Solution:
    def largest(self, arr):
        # code here
        # return max(arr)
        res = arr[0]
        n = len(arr)

        for i in range(n-1):
            if arr[i+1] > res:
                res = arr[i+1]
        return res

obj = Solution()
print(obj.largest([1,100,7,56,90])) 

