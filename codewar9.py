# Moving Zeros To The End

def move_zeros(lst):
  l = []
  count = 0 
  for i in lst:
    if i == 0 :
      count += 1
    else :
      l.append(i)


  while count != 0 :
    l.append(0)
    count -= 1

  return l 

print(move_zeros([0,0]))

# def move_zeros(lst):
#     return [x for x in lst if x != 0] + [0] * lst.count(0)

# print(move_zeros([0, 0]))