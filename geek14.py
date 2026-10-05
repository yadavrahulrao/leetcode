#selection sort 

class Solution:
    def selectionSort(self,arr):
        # ascending order
        # n = len(arr)
        # for i in range(0,n):
        #     idx = i 
        #     for j in range(i+1, n):
        #         if arr[j] < arr[idx]:
        #             idx = j
        #     arr[i],arr[idx] = arr[idx] , arr[i]
        # return arr



        # descending order
        n = len(arr)
        for i in range(0,n):
            idx = i
            for j in range(i+1,n):
                if arr[idx] < arr[j] :
                    idx = j
            arr[i] , arr[idx] = arr[idx] , arr[i]
        return arr


obj = Solution()
print(obj.selectionSort([1,2,46,8,5,3,6]))