#  Merge sort

class Solution:
    
    def merge_array(self , left, right):
        res = []
        i = 0
        j = 0
        n = len(left)
        m = len(right)
        while i < n and j < m :
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else :
                res.append(right[j])
                j +=1 
        

        if i < n :
            while i < n :
                res.append(left[i])
                i +=1 

        if j < m :
            while j < m :
                res.append(right[j])
                j +=1 

        return res

    def mergeSort(self, arr):
        if len(arr) <= 1 :
            return arr
        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]
        left = self.mergeSort(l)
        right = self.mergeSort(r)
        return self.merge_array(left,right)


obj = Solution()
print(obj.mergeSort([4,1,3,9,7]))
            