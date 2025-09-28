# Story Title: “The Python Family Reunion”
# (Where every family member is a function with a different personality!)



# Meet Grandpa my_function. He’s retired, chill, and whenever you call him, he says the same thing:
# 👉 ‘Hello from a function!’
# Kind of like a grandpa who tells you the same joke every time — but we love him anyway
def my_function():
  print("Hello from a function")

my_function()



# This is a dad function with a lot of children. Every time you give him a fname, 
# he automatically gives them the family name Refsnes.
# He's super fair — treats all the kids equally, no favoritism!
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


# This function is super formal. First name? Last name? You better give both, or he refuses to talk.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


# If no one says where she’s from, she proudly says: ‘I am from Norway!’
# But if you tell her, she happily agrees!

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Chef Auntie can’t handle individual items —
# Give her a box (a list), and she’ll unpack it deliciously one by one.

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



# This guy doesn’t like to talk — just calculates quietly and gives you the answer.
# Give him a number, he gives you 5 times that.

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# This is the cousin who RSVP'd to the party… but never showed up.
# You leave a chair for them, but they never say or do anything.

def myfunction():
  pass



