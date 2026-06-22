#LIST
Bio=["Dhanya",4.5,50,'F']
print("List Values",Bio)
print(type(Bio))
#Adding the list new elements
#Append
Bio.append("Software developer")
print(Bio)
print(len(Bio))
#Adding new elements using insert method
Bio.insert(3,565)
print(Bio)
#Replace
Bio[5]="TeamLead"
print(Bio)
salary=[25000,65000,80000,90000]
print(min(salary))
print(max(salary))

print(sum(salary))
print(salary)
salary.remove(25000)
print(salary)
salary.pop()
print(salary)
salary.pop(1)
print(salary)
salary.reverse()
print(salary)



#List MEthod
#copy ,count
li=[25,45,55,85,44,10]
Copy=li.copy()
print(Copy)
count=li.count(55)
print(count)

# li=input("Enter the List values")
# list=li.split(",")
# print("list values")
# for i in list:
#     print(i)

#looping list
n=int(input("Enter The list"))
Empty_list=[]
for i in range(n):
    livalue=input("enter values of List")
    Empty_list.append(livalue)
print("LIST DATA",Empty_list)    

name={'Aswathi','Dhanya','Aishwarya','Asmitha','Dhanya'}
print(name)

#set constructor
place=set(('salem','Chennai',"Pondy"))
print(place)

#update set
alpha={'kumar','Raja','Deepika','Sathish'}
alpha.update('Mani')
print(alpha)

#update Set
a={'Coorg','Manali','Ooty','Kodaikanal'}
li=['Hari']
a.update(li)
print(a)

#remove Set
a={1,2,3,"sam","pk"}
a.remove("sam")
print(a)
a.discard(2)

print(a)

 
#pop method
s={"sam","pk","sathish","viji" }
s1=s.pop()
print(s1)
print(s)



#Access Set
a={"sam","pk","anu","sathish"}
for i in a:
    print(i)

#check the set is present or not
a={"sam","pk","anu","sathish"}
print("pk" in a)

# Name=("Asmitha","Aswathi","Dhanya","Aishwarya")
# print(Name)
# print(type(Name))

#SLicing
# print(Name[0:3])
# print(Name[:2])

#Tuple methods
# values=(145,45,55,68,95,1052)
# values1=values.count(145)
# print(values1)
# data=values.index(55)
# print(data)

#APpend MEthod
# college=('Psg','Kct','Karpagam','Gce')
# college1=list(college)
# college1.append('kiot')
# college=tuple(college1)
# print(college)

#Adding Tuple to Tuple
data=('Aishwarya','Dhanya','Aswathi')
data1=('Asmitha',)
data+=data1
print(data)

#join
place=('coorg','Ooty','Manali')
places=(123,45,66)
result=place+places
print(result)
#Join
place=('coorg','Ooty','Manali')
join=place*4
print(join)

#range
a=(12,45,'pk','sam')
for i in range(len(a)):
    print(a[i])

for i in a:
    print(a)
    
# a={"name":"sam","age":25,"name1":"samm"}
# print(a)
# print(a["age"])

# a={"name":"kumar","name1":"nandha","age":20}
# print(a)
# print(len(a))
# print(type(a))

# # #Adding Dict
# a={"name":"priya","age":27,"Hobbies":"chatting","frds":["Annamalai","priya","Gowthami"]}
# print(a)
# a["college"]="KCE"
# print(a)
# a.update({"Degree":"BE"})
# print(a)


bio={"Name":"Annamalai","Age":25,"Native":"salem"}
print(bio)
#clearMEthod
bio.clear()
print(bio)
print(bio)
#copyMEthod
bio={"Name":"Annamalai","Age":25,"Native":"salem"}
a=bio.copy()
print(a)
#get method
a=bio.get("Native")
print(a)
a=bio.get("car","Altroz")
print(bio)
print(a)
print(a)
#items method
a=bio.items()
print(a)
#key methid
a=bio.keys()
print(a)
a=bio.keys()
bio["hobby"]="chatting"
print(a)
#pop
bio.pop("Age")
print(bio)
a=bio.pop("Name")
print(a)
popitems
bio={"Name":"Annamalai","Age":25,"Native":"salem"}
print(bio)
bio.popitem()
print(bio)
#set default
a=bio.setdefault("frnds","pp")
print(a)
#update
bio.update({"car":"altroz"})
print(bio)
#values
a=bio.values()
print(a)
a=bio.values()
bio["CRH"]="pk"
print(a)


#Loop Dict
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
#print(a)
#key names
for i in a:
    print(i)
#values
for i in a:
    print(a[i])
#using values 
for i in a.values():
    print(i)
#using keys 
for i in a.keys():
    print(i)
#using items
for i,j in a.items():
    print(i,j)


#REMOVE 
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
a.pop("name")
print(a)
#del
del a["age"]
print(a)
#clear
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
a.clear()
print(a)


#GETTING DICT
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
b=a.items()
print(b)
#add dict
a["car"]="IGNIS"
print(b)
#check dict
if "name" in a:
    print("yes,do you have chatting with frnds ")

#COPY DICT

a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
b=a.copy()
print(b)
#using bulit fuction
b=dict(a)
print(b)


for i in range(0,10):
    print(i)


#change Dict
a={"name":"pp","age":25,"Hobbies":"chatting","frds":["sam","pk","rajesh"]}
print(a)
a["age"]=29
print(a)
#update dict
a.update({"name":"raja"})
print(a)

# def Place():
#     cooling_places=input("Enter The Places")
#     if cooling_places == "OOTY":
#         print("Don't Go ooty ")
#     elif cooling_places == "Kodaikanal":
#         print("Go with family then enjoy the Ride")
#     elif cooling_places =="Coorg":
#         print("Let enjoy")  
#     else:
#         print("Stay at home")
# Place()                  

#Function With Parameter

def prompt(qual,ref):
    if qual == 'ug' and ref == 'HR':
        print("you are in us based Team")
    elif qual == 'pg' and ref == 'TeamLead':
        print("You are in Russian baseD company")
    else:
        print("You are hired")
prompt(qual='ug',ref='HR')        
prompt('ug','HR')                
prompt(ref='TeamLead',qual="pg")
prompt('pg','TeamLead')

def Aiswarya():
    print("550 Marks")
Aiswarya()   
# with return

def add():
    alpha=150
    beta=300
    sum=alpha+beta
    return sum
print("The sum of numbers",add())  

#without return
def sum():
    alpha=100
    beta=580
    add=alpha+beta
    print("The sum ",add)
sum()
#With parameter
def college(clgname):
    print("sona",clgname)
college("College")    
       