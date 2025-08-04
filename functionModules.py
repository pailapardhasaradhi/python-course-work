data={'1234':{'balance':4561,'pin':123,'history':[]}
      '4567':{'balance':4554,'pin':456,'history':[]}
      '4589':{'balance':4554,'pin':456,'history':[]}
      '9011':{'balance':4554,'pin':456,'history':[]}
}
acc_num=None
login_status=False

def welcome():
    print('welcome to ATM')
def login(acc,pin):
    if acc_num in data:
        if data[acc]['pin']==pin:
            acc_num=acc
            login_status=True
            print("Login Successful")
        else:
            print("Invalid Login")
def check_balance():
    if login_status and acc_num:
        print(f"current Blance: {data[acc_num]['balance']}")
    else:
        print("Login Again")

    def deposit():
        if login_status and acc_num:
           amount=int(input("enter the amount to withdraw: "))
           data[acc_num]['balance']-=amount
           data[acc_num]['balance']

            
