#Two Sum
def two_sum(numbers, target):
    i = 0
    while i <= len(numbers):
      
        a = target - numbers[i]
        if a in numbers :
          if i != numbers.index(a):
            
            return i ,numbers.index(a) 
     
        
        i = i +1 
    

print(two_sum([1234,5678,9012], 14690))

