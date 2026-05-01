def max_sequence(arr):
  n = len(arr)
  curr = fix = 0
  for i in arr:
    curr = max(0,curr+i)
    fix = max(fix,curr)

  return fix

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

s = max_sequence(arr)
print(s)