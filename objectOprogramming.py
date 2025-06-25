class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive .")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance!")
    def check_balance(self):
        print(f"{self.account_holder}'s balance: {self.balance}")

my_account = BankAccount("Poline", 5000)
my_account.check_balance()
my_account.deposit(1000)
my_account.withdraw(6500)
name = input("Enter account holder name: ")
account = BankAccount(name)
while True:
    print("\n--- Bank Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == "1":
        account.check_balance()
    elif choice == "2":
        amount= float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "4":
        print("Thank you for using the bank system. Bye!")
        break
    else:
        print("Invalid choice!. Please select a valid option.")
