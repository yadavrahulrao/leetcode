# recursive bubble sort 

class Solution():
    def bubble_Sort(self, arr , n):
        if n <= 1:
            return 
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1] , arr[i]
        self.bubble_Sort(arr,n-1)
        return arr

obj = Solution()
print(obj.bubble_Sort([3,1,4,6,2],5))
        