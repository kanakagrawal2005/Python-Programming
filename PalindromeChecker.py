# Function to check palindrome
def check_palindrome(x):
    original = x
    reverse = ""

    # Using loop to reverse
    for ch in x:
        reverse = ch + reverse

    # Check using if-else
    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Input from user
value = input("Enter a number or string: ")

# Call function
check_palindrome(value)