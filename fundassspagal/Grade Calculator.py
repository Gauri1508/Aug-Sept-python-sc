marks = float(input("Enter your percentage to be GRADED :"))

if marks < 100:
    if marks <= 100 and marks > 80:
        print("A")
    elif marks <= 80 and marks > 60:
        print("B")
    elif marks <= 60 and marks > 40:
        print("C")
    elif marks <= 40 and marks > 35:
        print("D")
    elif marks <= 35:
        print("You've FaileZDD")
else:
    print("Please check the percentage it should be below 100")
