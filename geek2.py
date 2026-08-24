#Array Search
class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

obj = Solution()
print(obj.search([1,2,3,4],3))