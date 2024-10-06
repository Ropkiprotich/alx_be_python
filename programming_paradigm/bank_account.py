class BankAccount():
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount<=self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Your Current balance is: ${self.account_balance:.2f}")

def main():
    account = BankAccount()
    while True:
        bank_operation = input("Enter your type of transaction (deposit, withdraw or display)")

        if bank_operation == "deposit":
            amount=float(input("Enter amount:"))
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")

        elif bank_operation == "withdraw":
            amount=float(input("Enter amount:"))
            sucess =account.withdraw(amount)
            if sucess:
                print(f"Withdraw: ${amount:.2f}")
            else:
             print("insufficient balnce")

        elif bank_operation == "display":
            account.display_balance()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main() 