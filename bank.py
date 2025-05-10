accounts = {}

def create_account():
    name = input("Enter your name: ")
    if name in accounts:
        print("Account already exists.")
    else:
        accounts[name] = 0
        print(f"Account created for {name}.")

def check_balance():
    name = input("Enter your name: ")
    if name in accounts:
        print(f"Your balance is ₹{accounts[name]}")
    else:
        print("Account not found.")

def deposit():
    name = input("Enter your name: ")
    if name in accounts:
        amount = float(input("Enter amount to deposit: ₹"))
        accounts[name] += amount
        print(f"₹{amount} deposited. New balance: ₹{accounts[name]}")
    else:
        print("Account not found.")

def withdraw():
    name = input("Enter your name: ")
    if name in accounts:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= accounts[name]:
            accounts[name] -amount 
            print(f"₹{amount} withdrawn. New balance: ₹{accounts[name]}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

def main():
    while True:
        print("\n===== Mini Banking App =====")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            check_balance()
        elif choice == '3':
            deposit()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":