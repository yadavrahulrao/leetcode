from collections import Counter
def solve(s):
  freq = Counter(s)

  need = {c for c in freq if freq[c]%2 == 1}

  stack = []
  used = set()
  remain = Counter(s)

  for c in s :
    remain[c] -= 1

    if c not in need :
      continue 
    if c  in used:
      continue
    while stack and c < stack[-1] and remain[stack[-1]]> 0:
      used.remove(stack.pop())
    stack.append(c)
    used.add(c)
    
  
  return ''.join(stack)