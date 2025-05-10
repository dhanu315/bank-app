# Dictionary to store all accounts
accounts = {}
next_account_number = 1001

def create_account():
    global next_account_number
    name = input("enter your name:").strip()
    if not name:
        print("name cannot be empty.")
        return
    try:
        balance = float("enter initial balance(non-negative):")
        if balance < 0:
            print("initial balance must be non-nagative.")
            return
    except ValueError:
        print("invalid input.balance must be a number")
        return
              
    next_account_number += 1 
    account_number = next_account_number  

    
    accounts[account_number] ={
    "Name": name,
    "Balance": balance,
    "Transaction":[f"account created with balance:{balance}"]
 }
    print(f"account created successfully! account number: {account_number} ")


def deposit_money():
    acc_num = get_account_number
    if acc_num is None:
        return

    try:
        amount = float(input("enter the amount to deposit:"))
        if amount <=0:
            print("deposit amount must be positive")
            return
    except ValueError:
        print("invalid input,amount must be a number")
        return

    accounts[acc_num]["balance"] += amount
    accounts[acc_num]["transaction"].append(f"deposit d:{amount}")
    print("deposit successful")

def withdraw_money():
    acc_num = get_account_number
    if acc_num is None:
        return

    try:
        amount = float(input("enter the amount to withdraw:"))
        if amount <=0:
            print("withdraw amount must be positive")
        return
    except ValueError:
        print("invalid input,withraw must be a number")
        return
    
if amount > accounts[acc_num]["balance"]:
    print("insufficient balance")
    

accounts[acc_num]["balance"] -= amount
accounts[acc_num]["transactions"].append(f"withdraw:{amount}")
print("withdraw successful")  


def check_balance():
    acc_num = get_account_number()
    if acc_num is None:
        return

    balance = accounts[acc_num]["balance"]
    print(f"current balance for account{acc_num}:{balance}")



def transaction_history():
    acc_num = get_account_number()
    if acc_num is None:
     return

    print(f"transaction history for account{acc_num}:")
    for transaction in accounts[acc_num]["transaction"]:
     print("-",transaction)

def get_account_number():
    try:
        acc_num = int(input("enter account number:"))
        if acc_num is not accounts:
            print("account not found")
            return None 
        return acc_num 
    except ValueError:
        print("invalid account number:")
        return None


def main_menu():
    while True:
        print("\n=====Mini Banking System=====")
        print("1.create account")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.check balance")
        print("5.transaction history")
        print("6.exit")

choice = input("choose an option(1-6)")
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
    print("invalid choice, plese select a valid option")

    if__name__ == "__main__"
    main_menu()





    
    


            



