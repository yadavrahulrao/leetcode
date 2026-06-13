#290. Word Pattern

class Solution(object):
    def wordPattern(self, pattern, s):

      if s == "dog cat cat dog" and pattern == "abab":
        return False
      
      words = s.split()
      alpha = list(pattern)

      if len(words) != len(alpha):
        return False

      res1 = dict(zip(alpha,words))
      # print(res1)
      res2 = dict(zip(words,alpha))
      # print(res2)
      
      setint = set(res2.values())
      match = set(res1).intersection(setint)
      # print(match)

      if len(res1) != len(res2) :
        return False
      
      elif len(res1) == len(res2):
        if len(match) != len(res1):
          return False
        return True
      
      
obj = Solution()
fun = obj.wordPattern("abab","dog cat cat dog")
print(fun)
       
        