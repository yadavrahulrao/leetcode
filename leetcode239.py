#605. Can Place Flowers


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 1
        for i in flowerbed:
            if i == 0:
                count += 1
            else :
                n -= (count - 1)//2
                count = 0
        count += 1
        n -= (count -1)//2
        
        if n <= 0 :
            return True
        return False
    
obj = Solution()
print(obj.canPlaceFlowers([1,0,0,0,1],0))
                
                
        
        