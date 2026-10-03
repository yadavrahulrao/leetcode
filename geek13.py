#Frequencies in a Limited Array

# class Solution:
#     def frequencyCount(self, arr):
#         #  code here
#         list1 = []
#         for i in range(1,len(arr)+1):
#             list1.append(i)

#         list2 = [0] * (len(arr)+1)
#         for i in arr:
#             list2[i] += 1
#         list3 = []
#         for i in list1 :
#             if i < 1 or i > 10 :
#                 return 0 
#             else:
#                 list3.append(list2[i])
                
#         return list3
    

# obj = Solution()

# print(obj.frequencyCount([1,2,2,3,5]))



class Solution():
    def ascaii_value(self,s,o):
        
        list1 = [0] * (len(s))
        for i in s :
            asc_val = ord(i)
            index = asc_val - 97
            list1[index] +=1

        for i in o :
            asc_val2 = ord(i)
            index2 = asc_val2 - 97

        return list1[index2]
        

obj = Solution()
print(obj.ascaii_value("aaa",["a"]))


