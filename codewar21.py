#Multiples of 3 or 5


def solution(number):
    res = []
    if number <= 0 :
        return 0
    
    for i in range(1,number):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)
    
    s = list(set(res))
    sums = sum(s)
    return sums
print(solution(4))