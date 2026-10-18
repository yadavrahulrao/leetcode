# Second Largest Number

def getSecondOrderElements(n,a):
    # Write your code here
    list1 = []
    if n == 2 :
        a.sort()
        list1.append(a[0])
        list1.append(a[1])
    if n > 2 :
        a.sort()
        list1.append(a[1])
        list1.append(a[-2])
    return list1
    

print(getSecondOrderElements(2,[1,7]))
