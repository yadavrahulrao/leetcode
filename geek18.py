# x = [1, True ,  False , 0]
# print(x.count(True))


# class Solution():
#     def string_count(self , s):
#         arr = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#         count = 1
#         words = s.split()
#         list2 = set(words)
#         s = " ".join(list2)
#         list1 = list(s)
#         for i in list1 :
#             if i == " ":
#                 count += 1
#             if i in arr :
#                 count -= 1
#         return count
            
# obj = Solution()
# print(obj.string_count("Yamaha is a mobility company. Yamaha builds great motors!"))




#quick sort 

class Solution:
    def quickSort(self, arr, low, high):
        if low < high :
            idx = self.partition(arr,low , high)
            self.quickSort(arr,low,idx-1)
            self.quickSort(arr, idx+1 , high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low
        j = high
        while i < j :
            while arr[i] <= pivot and i <= high -1 :
                i +=1 
            while arr[j] > pivot and j >= low +1 :
                j -= 1
            if i < j :
                arr[i] , arr[j] = arr[j] , arr[i]
        arr[low] , arr[j] = arr[j] , arr[low]
        return j 

obj = Solution()
print(obj.quickSort([4,1,3,9,7],0,4))