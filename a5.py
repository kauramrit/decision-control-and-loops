#Q.1- Take an input year from user and decide whether it is a leap year or not.

yr=int(input("enter year"))
if ((yr%400==0) or ((yr%4==0) and (yr%100!=0))):
    print(yr," is leap year")
else:
    print(yr," is not leap year")

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.

length=int(input("enter length"))
breadth=int(input("enter breadth"))
if(length==breadth):
    print("the dimensions are of square")
else:
    print("the dimensions are of rectangle") 

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

a1=int(input("enter age of 1st person"))
a2=int(input("enter age of 2nd person"))
a3=int(input("enter age of 3rd person"))
if(a1>a2)and(a1>a3):
    print("a1 is the oldest")
if(a2>a1)and(a2>a3):
    print("a2 is the oldest")
if(a3>a1)and(a3>a2):
    print("a3 is the oldest")
if(a1<a2)and(a1<a3):
    print("a1 is the youngest")
if(a2<a1)and(a2<a3):
    print("a2 is the youngest")
if(a3<a2)and(a3<a1):
    print("a3 is the youngest")

#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

#1. if employee is female, then she will work only in urban areas. 
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
#4. And any other input of age should print "ERROR".

age=int(input("enter age"))
sex=input("enter sex in M or F")
status=input("input ur martial status in Y or N")
if(sex=='F'):
    print("she can work only in urban areas")
if(sex=='M')and(age>=20 and age <40):
    print("he may work in anywhere")
if(sex=='M')and(age>=40 and age <60):
    print("he will work in urban areas only")
if age<20 or age>60:
    print("ERROR")

#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity=int(input("enter quantity"))
cost=quantity*100
if cost>1000:
    p=cost-(cost*0.1)
else:
    p=cost
print(p)
                              #LOOP
#Q.1- Take 10 integers from user and print it on screen.

for i in range(10):
    d=int(input("enter elemnts"))
    print(d)

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.

c=0
while(c!=5):
    c=c+1
    if(c==5):
        c=c+1
        continue
        print(c)

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

a=[]
b=[]
n=int(input("enter no of elements"))
for i in range(n):
    d=int(input("enter elemnts"))
    a.append(d)
print(a)
for i in a:
    b.append(i**2)
print(b)
   
#Q.4- From a list containing ints, strings and floats, make three lists to store them separately

a=[1,4,6.7,'r','i',8.9]
b=[]
c=[]
d=[]
for i in a:
    if isinstance(i,int):
        b.append(i)
    elif isinstance(i,str):
        c.append(i)
    elif isinstance(i,float):
        d.append(i)
print("integer list:",b)
print("float list:",d)
print("string list:",c)
    


#Q.5- Using range(1,101), make a list containing only prime numbers.

flag=0
a=[]
for i in range(1,101):
    flag=0
    for j in range(2,int(i/2)):
        if i%j==0:
            flag=1
            break
    if(flag==0):
        print(i)
        a.append(i)
print(a)

#Q.6- Print the following patterns:
#   *
#   **
#   ***
#   ****

for i in range(0,4):
    for j in range(0,i+1):
        print("*",end="")
    print("\n")
  
#Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

c=[]
a=int(input("enter no of elements"))
for i in range(a):
    b=int(input("enter elements"))
    c.append(b)
d=int(input("enter element to be deleted"))
for i in c:
    if i==d:
        c.remove(d)
print(c)    




