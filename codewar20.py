# Array plus array

def array_plus_array(arr1,arr2):
    lst = arr1 + arr2
    # pos = list(map(abs,lst))
    res = sum(lst)
    return res

print(array_plus_array([-1, -2, -3], [-4, -5, -6]))
