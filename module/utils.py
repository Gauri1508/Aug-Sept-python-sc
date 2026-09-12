def find_max():
    number = []
    number = input("enter list items :",)
    new_number = number.split(",")
    max = new_number[0]
    for num in new_number:
        if num > max:
            max = num
    print(max)


# find_max()
