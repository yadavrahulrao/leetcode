#  Merge sort

class Solution:
    
    def merge_array(self , arr , l , mid,r):
        res = []
        i = l
        j = mid + 1
        
        while i <= mid and j <= r :
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i += 1
            else :
                res.append(arr[j])
                j +=1 
        while i <= mid :
            res.append(arr[i])
            i +=1 

        
        while j <= r :
            res.append(arr[j])
            j +=1 

        for k in range(len(res)):
            arr[l+k] = res[k]

    def mergeSort(self, arr,l,r):
        if l>= r :
            return 
        mid = l + (r- l)//2
        
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge_array(arr,l,mid,r)
    
        # def merge_array(self,left,right):
        #     res = []
        #     i = 0
        #     j = 0
        #     n = len(left)
        #     m = len(right)
        #     while i <n and j <m :
        #         if left[i] < right[j]:
        #             res.append(left[i])
        #             i += 1
        #         else :
        #             res.append(right[j])
        #             j +=1 
        #     if i < n :
        #         while i < n :
        #             res.append(left[i])
        #             i +=1
        #     if j < m :
        #         while j < m :
        #             res.append(right[j])
        #             j += 1
        #     return res
        
        # def mergeSort(self, arr,l,r):
        #     if len(arr) <= 1:
        #         return arr
                
        #     mid = len(arr) // 2
        #     a = arr[:mid]
        #     b = arr[mid:]
        #     left = self.mergeSort(a,l,r)
        #     right = self.mergeSort(b,l, r)
        #     return self.merge_array(left,right)
        
        # code here


obj = Solution()
arr = [4,1,3,9,7]
obj.mergeSort(arr,0,len(arr)-1)
print(arr)
            