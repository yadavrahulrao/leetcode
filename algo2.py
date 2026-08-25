#binary search algorithm

class Solution():
    def binary(slef , arr , x):
        low = 0
        high = len(arr) -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == x :
                return mid
            elif arr[mid] < x:
                low  = mid +1 

            else :
                high = mid -1

        return -1
obj = Solution()
print(obj.binary([1,2,4,5,6,7,9],5))