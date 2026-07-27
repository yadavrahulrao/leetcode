#374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        
        l, r= 1, n

        while True:
            mid = (l + r) // 2
            res = guess(mid)

            if res == 0:
                return mid

            if res == -1:
                r = mid - 1
            else:
                l = mid + 1
        