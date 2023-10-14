class BankAccount(object):
    defaultAccNumber = 1

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1

    def deposit(self, amount):
        self.balance += amount
        print(f'You deposited amount is {amount}')

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough balance!')
        else:
            self.balance -= amount
            print(f'You withdrawal amount is {amount}')

    def getBalance(self):
        return self.balance

if __name__ == '__main__':
    name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    myObj = BankAccount(name, initial_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Enter the deposit amount: "))
            myObj.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: "))
            myObj.withdraw(amount)
        elif choice == '3':
            print(f"Balance: {myObj.getBalance()}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
