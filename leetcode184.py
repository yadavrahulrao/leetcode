#1700. Number of Students Unable to Eat Lunch

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count = [0,0]

        for s in students:
          count[s] +=1
        
        for f in sandwiches:
          if count[f] == 0:
            break
          count[f] -= 1

        return count[0] + count[1]