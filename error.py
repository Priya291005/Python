# a=100
# b=0
# c=a/b
# print(c)

# try:
#     a=100
#     b=0
#     c=a/b
#     print(c)
    
# except Exception as e:
#     print(e)
#     print("Asmitha")    
#Error types:
# syntax Error
# Intentation error   
# NameError
# KeyERROR
# Typeerror
# VALUE ERROR
# INDEX ERROR
# ZERO DIVISION ERROR

#name ERROR
#Name=458
#print(name)
# try:
#     name=input("Enter the Name")
#     print(namee)
    
# except NameError as e:
#     print(e)
#     name=input("Enter the Name")
#     print(name)
#     print("variable name  not defined ")

#Value Error
# try:
#     num=int(input("Enter the Number"))
#     print(num)
# except ValueError as e:
#     print("Value error",e)
#     print("Asmitha")    


 #Type Error

# try:
#     data="150"+6
#     print(data)
# except TypeError as e:
#     print(e)    
    # print("kumar"+"Raja")
#Index Error:
try:
    li=[14,45,78,96,96]
    print(li[7])
except IndexError as e:
    print("Index Error",e)
    print(li[1])    

#Key Error
try:
    alpha={"Name":"Annamalai","age":30}
    print(alpha['Name1'])
except KeyError as e:
    print("KEY ERROR ",e)
    print(alpha['Name'])