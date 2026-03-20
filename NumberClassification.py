# Function to classify a number
def classify_number(num):
    
    # Check Positive / Negative / Zero
    if num > 0:
        print(num, "is Positive", end=", ")
        
        # Nested if for Even / Odd
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
            
    elif num < 0:
        print(num, "is Negative", end=", ")
        
        # Nested if for Even / Odd
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
            
    else:
        print(num, "is Zero")

# Taking list input manually
numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Processing all numbers using for loop
for num in numbers:
    classify_number(num)