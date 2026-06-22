#Next bigger number with the same digits

from itertools import permutations

def next_bigger(n):

    # if n >= 0 and n <= 11:
    #   return -1

    # elif n == 9876543210 :
    #   return -1

    # elif n == 7193887742200:
    #   return 7194002237788

    # elif n >= 12 and n <= 98 :
    #   digit = [int(d) for d in str(n)]
    #   digit.reverse()
    #   res = "".join(map(str,digit))
    #   if  int(res) <= int(n) :
    #     return -1
    #   else :
    #     return int(res)

    # else :
    #   stn = str(n)
    #   pem = [int("".join(p)) for p in permutations(stn)]
    #   final = min([j for j in pem if j > int(n)])
    #   return final


    dig = list(str(n))
    idx = -1
    for i in range(len(dig)-2 , -1 , -1):
      if dig[i] < dig[i+1]:
        idx = i
        break

    if idx == -1 :
      return -1 
    
    for j in range(len(dig)-1 , idx , -1 ):
      if dig[j] > dig[idx]:
        dig[idx] , dig[j] = dig[j] , dig[idx]
        break

    l = dig[:idx + 1]
    r = sorted(dig[idx + 1 :])

    return int("".join(l + r))    
print(next_bigger(513))