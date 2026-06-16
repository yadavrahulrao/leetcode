#383. Ransom Note
from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):

      count_mag = [char.lower() for char in magazine if char.isalpha()]
      feq_mag = Counter(count_mag)
      m = dict(feq_mag)

      count_ran = [j.lower() for j in ransomNote if j.isalpha()]
      feq_ran = Counter(count_ran)
      r = dict(feq_ran)

      def subset(m,r):
        for letter , freq in r.items():
          if letter not in m or m[letter] < freq :
            return False
        return True

      return subset(m,r)


    
obj = Solution()
print(obj.canConstruct("a","b"))
