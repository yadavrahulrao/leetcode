#Ninja want to add coding to his skill set so he started learning it.
#  On the first day, he stuck to a problem in which he has given a long integer ‘X’ 
# and had to count the number of digits in it.


def countDigit(n:int) -> int :
    s = str(n)
    list1 = []
    for i in s :
        list1.append(i)
    return len(list1)
print(countDigit(89))


