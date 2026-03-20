
i=0
while i<3:
    username = input("Enter username")
    password = input("Enter password")

    if username=="admin" and password=="1234" :
        print("Login successful")
        break
    else:
        print("Wrong Info")
        i+=1

if(i==3):
    print("Account Locked")

    

