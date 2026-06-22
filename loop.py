1 < 5
0
1 
2 
3 
4

#FOR:
for name in "Dhanya":
    print(name)

#Orders
# order=[200,500,200,150,400]
# total=0
# for price in order:
#     total+=price

# print("Total",total)   


#EVen Number
# even=[2,10,15,16,18,30,50,1]
# for a in even:
#     if a%2==0:
#         print("Even number ",a)
#     else:
#         print("ODD number",a)    


#FOR IN RANGE
for hello in range(1,10):
    print(hello)
#Tables:
table=int(input("Enter Table Number"))
for i in range(1,11):
    print(f"{table}*{i}={table*i}")
    
    # Syntax:
# while(condition):
#     stmts

#     Do.while:
#  do 
# {
#     print("Asmitha")
#     stmts
# }while(condition)   





#ATM PIN
# correct_pin="1234"
# Re_type=""
# while Re_type!=correct_pin:
#     Re_type=input("Enter Re_type Pin")
# print("Accessed")  

#Theater Seats:
# seat=1
# while seat <=18:
#     amount=int(input("Enter The Amount "))
#     if amount >=200:
#         print("SEAT BOOKED @",seat)
#         seat+=1
#     else:
#         print("Insufficient Balance")    

 
# hire =5
# while hire > 0:
#     skills=input("enter the skills")
#     project=int(input("How manu Project Do you have"))
#     if skills == 'python' or project >5:
#         print("You are Hired" )
#     elif skills == 'Java' or project >=10:
#         print("You are eligible to Team lead")    
#         hire-=1
#     else:
#         print("Thank you .......Tata Bye BYe")   

hire =5
while hire > 0:
    skills=input("enter the skills")
    project=int(input("How many Project Do you have"))
    if (skills == 'python' or skills == 'java') and project >5:
        print("You are Hired" )
        hire-=1
    else: 
        print("try to upgrade Skills ")        