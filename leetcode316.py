#3723. Maximize Sum of Squares of Digits


class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num or sum == 0:
            return ""
        rem = sum % 9
        digit = sum // 9
        arr = []
        for i in range(digit):
            
            arr.append("9")
        if rem > 0 :
            arr.append(str(rem))

        while len(arr) < num:
            arr.append("0")
        return "".join(arr)
    

obj = Solution()
print(obj.maxSumOfSquares(2,17))


        