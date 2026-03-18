# Count the no of special symbol
# import re
# var = 'gasgg54@#vscsd!s*'
# count = 0
# for i in var:
#     # z = re.findall('[a-z,0-9]',i)
#     z = ord(i)
#     # print(z)
#     # if z:
#     if z >= 97 and z <= 122:
#         continue
#     elif z >= 48 and z <= 57:
#         continue
#     else:
#         count += 1
# print(count)


# find the interaction of three arrays
# input = [1,2,3], [2,3,4], [3,4,5]
# output = 3\

# A = [1,2,3]
# B = [2,3,4]
# C = [3,4,5]

# for i in A:
#     if i in B and i in C:
#         print(i)

# Move zeros to the end 
# input = [0,1,0,3,12]
# output = [1,3,12,0,0]

# a = [0,1,0,3,12]
# for i in a:
#     if i == 0:
#         a.remove(i)
#         a.append(i)
# print(a)

#find the second largest element

# a = [7,3,9,2,8]
# a.sort()
# print(a)
# print(a[-2])
n = int(input())
list = []
for i  in range(n):
    a = int(input("Enter elements:"))
    list.append(a)
count = 0

for j in range(len(list) - 1):
    distance = abs(list[j] - list[j+1])
    count += distance

print(count) 
