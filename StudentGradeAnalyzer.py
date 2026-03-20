# Taking input 5 times
for i in range(1, 6):
    marks = int(input("Enter your marks: "))

    if marks >= 90:
        print("A+")
    elif 75 <= marks <= 89:
        print("B")
    elif 50 <= marks <= 74:
        print("C")
    else:
        print("Fail")