#Sum of Intervals

def sum_of_intervals(intervals):
    intervals = sorted(intervals)
    sum = 0 
    a,b = intervals[0]
    for i,j in intervals[1:]:
      if i <= b :
        b = max(b,j)
      else :
        sum += b - a
        a,b = i , j 
      


    return sum + (b-a)

print(sum_of_intervals([
   [1, 5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ))

