#write a program to remove duplicate in a list
num = [2, 3, 4, 5, 3, 2, 4]
seen = []
for i in num:    
    if i not in seen:
        seen.append(i)
    else:
        print(i)
'''    if num[i] in temp:
        print(num[i])
    else:
        temp.append(i)
'''
