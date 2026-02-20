import os
class BankAcc:
    total_bank_balance = 0
    total_accounts = 0
    bank_name = "Mera Bank"
    def __init__(self: object, account_holder: str, initial_balance=0) -> None:
        self.account_holder = account_holder
        self.balance = initial_balance
        BankAcc.total_accounts += 1
        BankAcc.total_bank_balance += initial_balance
    def deposit(self: object,amt: float) -> None:
        if amt > 0:
            self.balance += amt
            BankAcc.total_bank_balance+=amt
        else: 
            return
        print(f"Current Balance is Rs{self.balance}")
    def withdraw(self: object, amt: float) -> None:
        if(self.balance-amt) >= 0:
            self.balance -= amt
            BankAcc.total_bank_balance -= amt
            print(f"Current Balance is Rs{self.balance}")
            input("Press Enter to continue...")
            return
        else:
            print(f"Insufficient Balance")
            input("Press Enter to continue...")
            return
    def accInfo(self: object) -> None:
        print(f"Bank Name: {self.bank_name}")
        print(f"Acc holder Name: {self.account_holder}")
        print(f"Current Balance is Rs{self.balance}")
        input("Press Enter to continue...")
    def bankInfo(self: object) -> None:
        print(f"Bank Name: {self.bank_name}")
        print(f"Total Accounts: {self.total_accounts}")
        print(f"Total Bank Balance: Rs{self.total_bank_balance}")
        input("Press Enter to continue...")

def main():
    while(1):
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Info")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter account holder name: ")
            initial_deposit = int(input("Enter initial deposit amount: "))
            acc = BankAcc(name, initial_deposit)
            print(f"Account created successfully for {name} with initial balance Rs{initial_deposit}")
        elif choice == 2:
            amt = int(input("Enter amount to deposit: "))
            acc.deposit(amt)
        elif choice == 3:
            amt = int(input("Enter amount to withdraw: "))
            acc.withdraw(amt)
        elif choice == 4:
            acc.accInfo()
        elif choice == 5:
            print("Exiting...")
            break
        elif choice == 6:
            BankAcc.bankInfo(acc)
        else:
            print("Invalid choice! Please try again.")
        #clear the console after each operation
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
if __name__ == "__main__":    main()