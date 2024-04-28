import random
# Built-in Python Data types

# Text Type str
print(type("hello"))
# Numeric Types:	int, float, complex
print(type(1),type(1.0),type(1j))

a,b,c=1,1.5,1j
x,y,z=float(a),int(b),complex(a)
print(x,y,z)

print(random.randrange(1,10))

# Sequence Types:	list, tuple, range
print(["apple", "banana", "cherry"])
print(("apple", "banana", "cherry"))
print(range(6))
# Mapping Type:	dict
Dict = {1: 'python', 2: 'is', 3: 'powerful'} 
print("\nDictionary with the use of Integer Keys: ") 
print(Dict) 
# Set Types:	set, frozenset
set1 = set("python") 
print("\nSet with the use of String: ") 
print(set1) 
set2 = {"apple", "banana", "cherry"}
frozenset = frozenset(set2)
# Boolean Type:	bool
print(type(True)) 
print(type(False)) 

# Binary Types:	bytes, bytearray, memoryview
print(type(b"hello"))
print(bytearray(5))
print(memoryview(bytes(5)))
# None Type:	NoneType
print(None)



# --------


# casting

int(1.1)

# python strings
str_1 = 'Hello'
mul_str = """python
is
simple"""

print("very,good"[1])

for i in "python":
    print(i)

print(len(str_1))

print('el' in str_1)
print('ok' not in str_1)

# slice strings

str_2=" Hello,Python!"
print(str_2[2:5])
print(str_2[:5])
print(str_2[2:])
print(str_2[-2:-5])
print(str_2.lower())
print(str_2.strip())
print(str_2.replace('Hello',"Hi"))
print(str_2.split(','))

print('Hi'+'Lucy')
print('Hi'+ ' ' + 'Lucy')

age=18
result = f"i am {age}"
print(result)

price=8
print(f"the price is {price:.2f} dollars")
print(f"the price is {3*7} dollars")

txt = "We are the so-called \"Vikings\" from the north."

# String Methods


# Specific Data Type

n= str('123')
int(20)
float(1.5)
complex(1j)
list(('a','b','c'))
tuple(('a','b','c'))
range(6)
dict(name='jack',age=18)
set(('a','b','c'))
# z= frozenset(("apple", "banana", "cherry"))
bool(5)
bytes(2)
bytearray(4)
memoryview(bytes(5))



# Object
class Student:
    name ='tom'
    def __init__(self,score):
        self.score = score

a = Student(100)
b= Student(80)

print(a.name,b.name,a.score)
print(Student.name)


# https://docs.python.org/zh-cn/3.12/tutorial/datastructures.html#

