# class Solution():
#     def salary(self , basic):
#         gross_salary = 0
#         if basic < 1000 :
#             HR = 15
#             DA = 70
#             gross_salary = basic + ((basic * HR)//100) + ((basic*DA)//100)
            

#         else : 
#             HR = 20
#             DA = 80
#             gross_salary = basic + ((basic * HR)//100)  + ((basic * DA)//100)
#         return gross_salary

# obj = Solution()
# print(obj.salary(1200))

         

class Solution():
    def palindrome(self, s):
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r :
            if s[l] != s[r] :
                return False
            l += 1
            r -= 1
        return True
obj = Solution()
print(obj.palindrome("Radar"))
