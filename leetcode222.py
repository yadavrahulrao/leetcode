#405. Convert a Number to Hexadecimal

class Solution(object):
    def toHex(self, num):
      if num == 0 :
        return '0'

      hex = '0123456789abcdef'
      res = []
      for i in range(7,-1,-1):
        val = (num >> (4* i)) & 0xF
        if res or val != 0 :
          res.append(hex[val])
      return "".join(res)

obj = Solution()

print(obj.toHex(26))
       
        