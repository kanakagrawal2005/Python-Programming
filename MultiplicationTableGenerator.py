# Function to generate multiplication table
def table(num):
    # Restrict negative input
    if num < 0:
        print("Negative numbers are not allowed")
    else:
        print(f"Multiplication table of {num}:")
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

# Taking input from user
number = int(input("Enter a number: "))

# Calling function
table(number)