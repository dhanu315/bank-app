accounts = {}
next_account_number = 1001

def get_account_number():
    try:
        acc_num = int(input("Enter account number:"))
        if acc_num not in accounts:
            print("Account not found")
            return None
        return acc_num 
    except ValueError:
        print("Invalid account number.")
        return None

def create_account():
    global next_account_number
    name = input("Enter your name:").strip()
    if not name:
        print("Name cannot be empty.")
        return
    try:
        balance = float(input("Enter initial balance (non-negative):"))
        if balance < 0:
            print("Initial balance must be non-negative.")
            return
    except ValueError:
        print("Invalid input. Balance must be a number.")
        return
              
    next_account_number += 1 
    account_number = next_account_number  

    accounts[account_number] ={
        "Name": name,
        "Balance": balance,
        "Transaction": [f"Account created with balance: {balance}"]
    }
    print(f"Account created successfully! {accounts}")

def deposit_money():
    acc_num = get_account_number()
    if acc_num is None:
        return
    try:
        amount = float(input("Enter the amount to deposit:"))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        accounts[acc_num]["Balance"] += amount
        accounts[acc_num]["Transaction"].append(f"Deposit: {amount}")
        print("Deposit successful.")
    except ValueError:
        print("Invalid input. Amount must be a number.")
        return

def withdraw_money():
    acc_num = get_account_number()
    if acc_num is None:
        return
    try:
        amount = float(input("Enter the amount to withdraw:"))
        if amount <= 0:
            print("Withdraw amount must be positive.")
            return
        if amount > accounts[acc_num]["Balance"]:
            print("Insufficient balance.")
            return
        accounts[acc_num]["Balance"] -= amount
        accounts[acc_num]["Transaction"].append(f"Withdraw: {amount}")
        print("Withdraw successful.")
    except ValueError:
        print("Invalid input. Amount must be a number.")
        return

def check_balance():
    acc_num = get_account_number()
    if acc_num is None:
        return
    balance = accounts[acc_num]["Balance"]
    print(f"Current balance for account {acc_num}: {balance}")

def transaction_history():
    acc_num = get_account_number()
    if acc_num is None:
        return
    print(f"Transaction history for account {acc_num}:")
    for transaction in accounts[acc_num]["Transaction"]:
        print("-", transaction)

def main_menu():
    while True:
        print("\n===== Mini Banking System =====")
        print("1. Create account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. Transaction history")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")
        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            transaction_history()
        elif choice == "6":
            exit()
        else:
            print("Invalid choice, please select a valid option.")

main_menu()
