#How many numbers III?

from itertools import combinations_with_replacement

def find_all(sum_dig, digs):
  s = combinations_with_replacement(range(1,10),digs)
  lst =[]
  for i in s :
    lst.append(i)
  a = []
  for i in lst:
    if sum(i) == sum_dig:
      n = int("".join(map(str,i)))
      a.append(n)
    
  if not a : 
    return []
  

  return [len(a),a[0],a[-1]]

    
    
print(find_all(10,3))