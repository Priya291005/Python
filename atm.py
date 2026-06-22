aval_bal=50000
def balance_check():
    print("Available Balance ,",aval_bal)
def deposit():
    global aval_bal
    amount=int(input("Enter AMount to Deposit"))
    if amount > 0:
        aval_bal+=amount
        print("Deposited successfully",amount)
        print("current balance",aval_bal)
    else:
        print("retype amount")   
def withdraw():
    global aval_bal 
    amount=int(input("Enter Amount to withdraw"))

    if amount <=0:
        print("Valid amount")
    elif amount <=aval_bal:
        aval_bal-=amount
        print("withdraw succefully")
        print("withdraw Balance",aval_bal)

    else:
        print("Insufficient Balance ")
def Atm():
    while True:
        print("\n Menu")
        print("1.balance check")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Back")

        choice=input("Enter choice:")
        if choice == "1":
            balance_check()     
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank for using HDFC ATM")
            break
        else:
            print("Invalid choice prefered")


Atm()