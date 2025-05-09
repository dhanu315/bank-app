accounts = {}

def create_account():
    name = input("enter your name")
    if name in accounts:
        print("account already exists")
    else:
        accounts(f"account [name] = 0")
        print(f"account create for {name}")

        cus_file=open("customer.txt",'w')
        cus_file.write(f"{cus_ID}\t")
        cus_file.write(f"{cus_pswrd}\t")
        cus_file.write(f"{cus_name}\t")
        cus_file.close()

        print("account created successful!")