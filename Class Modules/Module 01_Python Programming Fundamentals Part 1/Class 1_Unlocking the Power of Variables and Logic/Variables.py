x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# variable conversion
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Type checking
x = 5
y = "John"
print(type(x))
print(type(y))

# String format
x = "John"   
# is the same as
x = 'John'

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"


# multi variables in single line
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# same value in different variable 
x = y = z = "Orange"
print(x)
print(y)
print(z)


# list assigning
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


# string concatenating
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# sum
x = 5
y = 10
print(x + y)

# string can not be concatente with int
x = 5
y = "John"
print(x + y)


# Global Variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#########
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)




########
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



