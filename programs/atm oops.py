class ATM:
    def __init__(self):
        self.username = ["veera", "reddy"]
        self.password = ["1234", "1234"]
        self.balance = [500, 500]

class A(ATM):
    @staticmethod
    def withdraw(balance, i):
        amount = int(input("Enter amount to withdraw: "))
        balance[i] -= amount
        print("Your balance is:", balance[i])

    @staticmethod
    def change_password(password, i):
        new_password = input("Enter new password: ")
        password[i] = new_password
        print("Your new password is successfully updated.")

    @staticmethod
    def check_balance(balance, i):
        print("Your balance is:", balance[i])

class C(A, ATM):
    def __init__(self):
        super().__init__()
        name = input("Enter your name: ")
        if name in self.username:
            current_index = self.username.index(name)
            user_password = input("Enter your password: ")
            current_index1=self.password.index(user_password)
            if user_password == self.password[current_index1]:
                while True:
                    print("1. Withdraw\n2. Change Password\n3. Check Balance")
                    choice = int(input("Enter your choice: "))
                    if choice == 1:
                        self.withdraw(self.balance, current_index)
                    elif choice == 2:
                        self.change_password(self.password, current_index)
                    elif choice == 3:
                        self.check_balance(self.balance, current_index)
                    else:
                        print("Invalid choice.")
            else:
                print("Incorrect password.")
        else:
            print("Username not found.")

# Instantiate and run
user = C()









