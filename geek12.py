# counting of numbers using dictionary 



# nums = [1,1,2,3,5,6,8,9,4,5,3,5,6]
# x = int(input())
# dict_map = dict()

# for i in range(0,len(nums)):
#     if nums[i] in dict_map:
#         dict_map[nums[i]] += 1

#     else:
#         dict_map[nums[i]] = 1

# print(dict_map)



# hash_map = {}
# for i in range(0,len(nums)):
#     hash_map[nums[i]] = hash_map.get(nums[i],0) + 1

# print(hash_map)


# Frequency of Element


class Solution:
    def findFrequency(self, arr, x):
        # code here
        dict_map = {}
        for i in range(0,len(arr)):
            if arr[i] in dict_map:
                dict_map[arr[i]] += 1
            else:
                dict_map[arr[i]] = 1
        return dict_map.get(x,0)

obj = Solution()
print(obj.findFrequency([1,1,1,1,1],1))