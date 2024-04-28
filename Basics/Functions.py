# define

def functionName():
    # do something
    print('this is a function!')

# call

functionName()

def add(args1,args2):
    print(args1+args2)

add(1,2)


def square(args):
    return args*args

print(square(5))

def myFunc1(*args):
    print("the best language is",args[2])

myFunc1('java','php','python')

def myFunc2(args1,args2,args3):
    print("the best language is",args3)

myFunc2('java','php','python')

def myFunc3(**args):
    print("his last name is",args['lname'])

myFunc3(fname='bill',lname='gates')
