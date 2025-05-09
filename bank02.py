print("user_ID = 1010,Admin")

Admin_id =input("enter your id:")
cuss_id = "1001"
account = "1002"

while Admin_ID == '1010':
 
# admin_ID == '1010'
    print(".......BANKING APP.......")
    print("01.create customer")
    print("02.create account")
    print("03.deposit money")
    print("04.withraw money")
    print("05.check balance")
    print("06.transaction history")
    print("07.exit")

    choice= input('enter your option from[1-6]:')

    if choice == '1':
        cus_name = input("Enter your customer Name:")
        cus_pswrd = input("Enter your customer password:")
        Balance = input("enter your initial balance")
        cus_ID =1

        cus_file=open("customer.txt",'w')
        cus_file.write(f"{cus_ID}\t")
        cus_file.write(f"{cus_pswrd}\t")
        cus_file.write(f"{cus_name}\t")
        cus_file.close()
        print("Account created successfull")


    elif choice == '2':
        cus_ID = input("enter your customer ID:")
        cus_balance = int(input("enter initial balance:"))
        
        acc_file=open("account.txt",'a')
        acc_file.write(f"{admin_ID}\t")
        acc_file.write(f"{account}\t")
        acc_file.close()


    elif choice == '3':balance = 0 

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Deposited {amount}. New balance: {balance}")
    else:
        print("Deposit amount must be greater than zero.")


