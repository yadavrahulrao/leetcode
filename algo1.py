# fizz buzz algo -- in this we have to return fizz if a number is divisible by 3 and return buzz if
# divisible by 5 and by both then fizz buzz

num = [1,2,3,4,5]
for i in  num:
    if i % 3 == 0 and i % 5 == 0 :
        print("Fizz Buzz")
    elif i % 3 == 0 :
        print("Fizz")

    elif i % 5 == 0 :
        print("Buzz")
    else :
        print(i)