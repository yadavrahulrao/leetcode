#Exclamation marks series #1: Remove an exclamation mark from the end of string

def remove(s):
    list1 = list(s)
    if list1 and list1[-1] == "!":
        return "".join(list1[0:-1])
    else:
        return s
    
print(remove("hi!"))