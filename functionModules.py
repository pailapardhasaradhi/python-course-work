data = {
    '1234': {'balance': 4561, 'pin': 123, 'history': []},
    '4567': {'balance': 4554, 'pin': 456, 'history': []},
    '4589': {'balance': 4554, 'pin': 456, 'history': []},
    '9011': {'balance': 4554, 'pin': 456, 'history': []}
}

acc_num = None
login_status = False

def welcome():
    print('Welcome to ATM')

def login(acc, pin):
    global acc_num, login_status
    if acc in data:
        if data[acc]['pin'] == pin:
            acc_num = acc
            login_status = True
            print("Login Successful")
        else:
            print("Invalid PIN")
    else:
        print("Account not found")

def check_balance():
    if login_status and acc_num:
        print(f"Current Balance: {data[acc_num]['balance']}")
    else:
        print("Please login first")

def deposit():
    global data
    if login_status and acc_num:
        amount = int(input("Enter the amount to deposit: "))
        data[acc_num]['balance'] += amount
        data[acc_num]['history'].append(f"Deposited {amount}")
        print("Deposit Successful")
    else:
        print("Please login first")

def withdraw():
    global data
    if login_status and acc_num:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= data[acc_num]['balance']:
            data[acc_num]['balance'] -= amount
            data[acc_num]['history'].append(f"Withdrew {amount}")
            print("Withdrawal Successful")
        else:
            print("Insufficient funds")
    else:
        print("Please login first")

# Example run
welcome()
login('1234', 123)
check_balance()
deposit()
check_balance()
withdraw()
check_balance()
