# class Solution(object):
#     def firstMissingPositive(self, nums):
#       s = set(nums)
#       i = 1
#       while i in s :
#         i += 1
#       return i
# s = Solution()
# print(s.firstMissingPositive([1,2,0]))


#Strip Comments

def strip_comments(strng, markers):
   

    a = strng.split('\n')
    lst = []
    for i in a:
      for j in markers :
        if j in i:
          i = i.split(j)[0]
      lst.append(i.rstrip())

    return "\n".join(lst)

  
      
print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))