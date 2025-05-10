def get_customer_info():
    name = ("Enter customer name: ")
    address = ("Enter customer address: ")
    username = ("Enter customer username: ")
    password = ("Enter customer password: ")
    return

def create_customer():
    customer = get_customer_info()
    with open ("customer.txt",'a') as customer_file:
        customer_file.write(f"{customer[0]},{customer[1]}\n")

def get_next_customer_id ():
    with open ("customer.txt",'r') as cus_file:
        print(cus_file.read[-1].split (',')[0][1:])+1

if name 