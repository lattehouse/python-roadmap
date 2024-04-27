# create variables
a=5

b = "Apples"

# This is a comment

print(a,b)

# casting
c = str(3)
d = int(3)
e = float(3)

print(c,d,e)


# get the type

print(type(a),type(b),type(e))

# single  or double quotes

print("hello"=='hello')

f="hello"
F='python' # F will not overwrite f
print(f,F)
print(f+F)

# Variable Names

# legal
myname = 'Alex'
my_name = 'Alex'
_my_name = 'Alex' # Snake Case
myName = 'Alex' # Camel Case
MYNAME = 'Alex'
myname2 = 'Alex'
MyName='Alex' # Pascal Case


# illegal
# 2myname = 'alex'
# my-name = 'alex'
# my name = 'alex'


# Multiple Values
h,i,j='cat','dog','pig'

l=m=n='lower case'

fruits = ['orange','banana','litchi']
o,p,q=fruits
print(o,p,q)

# TODO Unpack Tuples:https://www.w3schools.com/python/python_tuples_unpack.asp


# output

print('python is awesome')
print('python','is','awesome') # best way
print('python'+'is'+'awesome')
print(1+2)
# error
# print(1+'ok')

# global variable
v='car'
def myfunc():
    v='airplane'
    print('I travel by',v)

myfunc()


# global keyword

def myRegion():
    global country
    country = 'China'
    print(country)
    
myRegion() # why this is necessary
print('i come from',country)
print(myRegion(),'is good')

    