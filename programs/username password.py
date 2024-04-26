user_name = "veerareddy"
user_password = 9901

name = input("enter your username : ")
if name == user_name:
    for i in range(1, 4):
        password = int(input("enter your password: "))
        if password == user_password:
            print("welcome")
            break
        else:
            print(f"{i}attempts is done\n {3 - i}attempts is done")
        if i == 3:
            print("hey you stupid your account is blocked now")
else:
    print("invalid username")
