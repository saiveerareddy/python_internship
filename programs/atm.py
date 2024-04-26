usernames = ["veera", "reddy", "sai"]
passwords = [1234, 1234, 1234]
balances = [500, 300, 500]

def withdraw(current):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balances[current]:
        balances[current] -= amount
        print("Your remaining balance is: ", balances[current])
        print("successfully withdrawn "+str(amount))
    else:
        print("Insufficient balance.")

def change_password(current):
    old_password = int(input("Enter old password: "))
    if old_password == passwords[current]:
        new_password = int(input("Enter new password: "))
        passwords[current] = new_password
        print("Your password is successfully changed.")
    else:
        print("Incorrect old password.")

def check_balance(current):
    print("Your balance is: ", balances[current])

name = input("Enter your username: ")
if name in usernames:
    current_index = usernames.index(name)
    user_password = int(input("Enter your password: "))
    if user_password == passwords[current_index]:
        while True:
            print("1. Withdraw\n2. Change Password\n3. Check Balance")
            choice = int(input("Enter your choice: "))
            data = {1: withdraw, 2: change_password, 3: check_balance}
            if choice in data:
                data[choice](current_index)
            else:
                print("Invalid choice.")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")



