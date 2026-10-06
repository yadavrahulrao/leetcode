# Bubble  sort 

class Solution:
    def bubbleSort(self,arr):
        # code here
        # n = len(arr)
        # for i in range(n-2 , -1 , -1):
        #     for j in range(0,i+1):
        #         if arr[j] > arr[j+1]:
        #             arr[j] , arr[j+1] = arr[j+1] , arr[j]

        # return arr



        # best case for bubble sort 
        n = len(arr)
        for i in range(n-2 , -1 , -1):
            ptr = False
            for j in range(0,i+1):
                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1 ] , arr[j]
                    ptr = True
            if ptr == False:
                break
        return arr


obj = Solution()
print(obj.bubbleSort([1,3,6,8,3,7,0,2]))

