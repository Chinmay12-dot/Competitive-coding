mylist = [["prasant", "ashjha"],['85.56'], [77 , "yyy"]]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[:])
# print(mylist[1:])
# print(mylist[1:4:2])
# print(mylist[::-1])

# mylist.append("Sujal")
# mylist.append("Chinu")
# mylist.append(69)

# mylist.insert(4,"hello")

# print(mylist)

# newlist = mylist.copy()
# print(newlist)
# print("example of multidimensional list:")
# print(mylist)
# # print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1 = ["Sujal","Chinu"]
# print(list1*2)
# list2=[50,41,52,'Chinu']
# # del list2[2]
# #print(list2)

# #del list2
# list2.clear()
# print(list2)

# name = "Prashant"
# print(name)
# myname = list(name) #typecasting
# print(myname)


# list3 = [44,69,22,53,31,41]
# list3.sort()
# print(list3)
# list3.sort(reverse=True)
# print(list3)

# math = 50
# phy = 50
# eng = 40
# print(id(math))
# print(id(phy))
# print(id(eng))

#aliasing
# mylist=[44,425,57,56]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

#looping
# name ='prahsant'
# print('Z' in name)
# print('Z' not in name)

# for i in range(2,21):
#     for j in range(1,11):
#         print(j*i," ",end="")
#     print("\n")
    

# for j in range(1, 11):
#     for i in range(2, 21):
#         print(f"{i*j:<4}", end="")
#     print()
    
# day = input("Enter any day: ")

# if day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
#     print(f"{day} is a Working Day")
# else:
#     print(f"{day} is Weekend")

#WAP to acct marks of 3 subject and calculate total marks and percentage if above 60 eligible for placement
# mark1 = float(input("Enter marks of subject 1: "))
# mark2 = float(input("Enter marks of subject 2: "))
# mark3 = float(input("Enter marks of subject 3: "))


# tot = mark1+mark2+mark3

# per = (tot/300) * 100

# print(f"Percentage: {per}")
# if(per >= 60):
#     print("Eligible")
# else:
#     print("Not Eligible")

# WAP to accpet 5 diff val in 5 diff and check max

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))
num5 = int(input("Enter num5: "))

if(num1 > num2 and num1 > num3 and num1 > num4 and num1> num5):
    print("Num1 is Greater")
elif(num2 > num1 and num2>num3 and num2>num4 and num2>num5):
    print("Num2 is Greater")
elif(num3 > num1 and num3>num2 and num3>num4 and num3>num5):
    print("Num3 is Greater")
elif(num4 > num1 and num4>num2 and num4>num3 and num4>num5):
    print("Num4 is Greater")
else:
    print("Num5 is Greater")