# Average Array

def avg_array(arrs):
    count = sum(1 for x in arrs if isinstance(x,list))
    cols = len(arrs[0])
    sums = [0] * cols
    for i in arrs:
      for j in range(cols):
        sums[j] += i[j]
    avg = [k/count for k in sums ]
    return avg
print(avg_array([[1, 2, 3, 4], [5, 6, 7, 8]]))


