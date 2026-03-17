# what will be the output of following code snippet

# fruit_list1=['Apple', 'Berry','Cherry','Papaya']
# fruit_list2= fruit_list1
# fruit_list3= fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1 , fruit_list2 , fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
# print(sum)    #output is 22


# def f(i,values = []):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)          #output is [1]  [1, 2]  [1, 2, 3]


# def func(value, values):
#     var = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# func(t,v)
# print(t, v[0])  #output is 3 44


# dict = {'c': 97, 'a': 96, 'b': 98}
# for _ in sorted(dict):
#     print(dict[_])  #output is 96 98 97


# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))   #output is 3

# product of array except self 
#given an array,return the product of each element except itself
# input [1,2,3,4]
# output [24,12,8,6]
# def productExceptSelf(arr):
#     n = len(arr)

#     res = [1] * n

#     for i in range(n):

#         for j in range(n):
#             if i != j:
#                 res[i] *= arr[j]

#     return res

# if __name__ == "__main__":
#     arr = [1, 2, 3, 4]
#     res = productExceptSelf(arr)
#     print(" ".join(map(str, res)))

