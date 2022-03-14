import math              #inbuilt modukes

# single line comment
'''multiline 
comment'''


print("Hello World")       #printing strings
print(math.gcd(3, 6))      #printing values

a = 10                     #variables in py
b = 20
print(a+b)

age = 10
if(age<18):            #if statement with use of indentation
    print("hello")

# pip install __module__name        in cmd 


#Arithmetic operations 
a = 10
b = "AloneMusk"
c = 34.55
d = 2
print(a + d)
print(a - d)
print(a * d)
print(a / d)
# ** is exponent
# // floor division
# % moduko


#Typecasting 
print("\t\tType Casting")
a = 52
b = 58.68
c = "Demo"
print(type(a))
print(type(b))
print(type(c))

from pydoc import stripid
from traceback import print_tb


e = 10                     #int
f = "10"                   #string


# typecasting
# convert no. string to int
print(int(f))
print(float(f))
name = "Ishaan"
name2 = "Berlin, Professor, Denver"
print(name[1])
print(name[2:5]) 
print(name.strip())
print(len(name))
var1 = name.lower()
var2 = name.upper()
print(var1, var2)
var = name.replace("an", "t")
print(var)
var3 = name2.replace(", ", "\n")
print(var3)


#string concatenation
str1 = "This is a"
str2 = " new car"
print(str1 + str2)


name1 = "ElonMusk"
name2 = "MarkZ"
temp = "{1} is a good man and {0} is also a good man".format(name1, name2)
# fstream 
temp2 = f"{name1} is a good man, {name2} too"
print(temp)
print(temp2)



# list 
lst = [21, 3, 5, 66, 64]
var5 = type(lst)
lst[2] = 41
var6 = len(lst)
lst.append(32)
lst.insert(1, 100)
lst.remove(66)
lst.pop()
del lst[3]
del lst
lst.clear 
print(var5)
print(var6)
print(lst)



# tuple 
a = ("Berlin", "Tokyo", "Helsinki")
var7 = type(a)
b = list(a)    #tuple to list
# cannot update the values of tuple
a[1] = "Professor"
print(a)
print(var7)



# set
s1 = {1, 3, 4, 5, 5, 5 ,5}
s1.add(222)
s1.update([12, 4, 55, 5, 484])
print(len(s1))
s1.remove(22)          #error
s1.discard(22)         #if present remove but no error when not present
# .pop, .clear, del
print(s1)



#dictionary 
RandomDict = {
    "Name" : "Random",
    "Marks" : 33,
    "School" : "DPS"
}
print(RandomDict)
RandomDict["Marks"] = 22
print(RandomDict["Marks"])
# .pop, .clear, del


# user input 
age  = input("Enter the age :")
print(age)     
age = int(age)       # tyoecasting
print(type(age))      #always string input



# conditional statments
if(age > 19):
    print("You are not a teen")
elif(age == 18):
    print("you are a awesome teen")
else:
    print("You are a teen")



from xmlrpc.client import boolean
# boolean
a = True
b = False


#loops
#for loop
lst = [1, 2, 23]
for i in range(0, 10):
    print(i)
for idx in lst:
    print(idx)
# use same for dictionary tuples set 

# while loop 
index = 0
while(index<20):
    if(index == 4):
        break                 # loop break
    if(index == 10):
        continue              #next iterations
    print(index)
    index = index + 1


#function with no return and values 
def greet():
    print("Good Morning!")

greet()

# function with return and values 
def sum(a, b):
    c = a + b
    return c

d = sum(12, 44)
print(d)


# object oriented programming
class Employee:
    def __init__(self, gname, gsalary):
        self.name = gname
        self.salary = gsalary

obj = Employee("Tokyo", 10000)                #object initialization
print(obj.name)
print(obj.salary)