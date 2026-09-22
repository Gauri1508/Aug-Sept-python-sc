# values = input("Enter 3 numbers: ")
# num = values.split(',')

# larg = num[0]
# for i in num:
#     if i > larg:
#         large = i
#         print(i)
#     elif i < larg

num1 = input("Enter 1st num :")
num2 = input("Enter 2nd num: ")
num3 = input("Enter 3rd num : ")

if num1 > num2 and num1 > num3:
    print(f"{num1} is largest")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the largest")
elif num3 > num1 and num3 > num2:
    print(f"{num3} is the largest")
