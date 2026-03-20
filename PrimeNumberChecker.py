def prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False   # Not prime
    return True            # Prime

number = int(input("Enter Number to check: "))
answer = prime(number)

if answer:
    print("Number is prime")
else:
    print("Number is not prime")