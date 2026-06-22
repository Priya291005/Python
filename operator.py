username="DHA"
password=1234
if username=="DHA" or password==1234:
    print("LOGIN SUCCESSFULLY")
else:
    print("LOG OUT")    

alpha=120
beta=220
print(alpha & beta)
print(alpha | beta)

# alpha=45
# beta=alpha
# print(beta)
# beta+=alpha
# print(beta)
# beta-=alpha
# print(beta)


#Average
total_marks=0
total_marks+=75 #maths
total_marks+=85 #science
total_marks+=95 #Computer
 
#calculate Average
Average=total_marks
Average/=3

Average+=10
Average+=20


print("Average",Average)

# alpha=float(input("Enter THe First number"))
# beta=float(input("enter The second Number"))

# print("Additon",alpha+beta)
# print("Subtract",alpha-beta)
# print("Multiplication",alpha*beta)
# print("Division",alpha/beta)
# print("Modulo",alpha%beta)



#BILLING 
# price=float(input("Enter product Price"))
# Quantity=int(input("Enter Product Quantity"))
# total=price*Quantity
# tax=total * 0.10
# final_amount=total+tax
# print("Final_Price",final_amount)

#Discount 
original_price=1500
discount=15
discout_percentage=(original_price*discount)/100

final_price=original_price-discout_percentage
print("Total price",final_price)
