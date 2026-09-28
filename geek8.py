# head recursion 


# def func(i,n):
#     if i>n :
#         return 
#     print(i)
#     func(i+1,n)

# func(1,5)


# tail recursion

# def func(i,n):
#     if i > n :
#         return 
#     func(i+1,n)
#     print(i)
# func(1,5)


# 1 to 5 using tail 

# def func(n):
#     if n == 0 :
#         return 
#     func(n-1)
#     print(n)

# func(5)




# 5 to 1 using head

# def func(n):
#     if n == 0 :
#         return 
#     print(n)
#     func(n-1)

# func(5)



#Sum of Natural Number Cubes

class Solution:
    def sumOfSeries(self,n):
        #code here
        if n == 1 :
            return 1
        return (n**3) + self.sumOfSeries(n-1)

obj = Solution()
print(obj.sumOfSeries(5))