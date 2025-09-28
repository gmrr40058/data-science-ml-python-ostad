# If logic
a = 33
b = 200
if b > a:
  print("b is greater than a")


# Indetation should be maintain. After each if statement, in next line, a tab (4 space) should be maintained.
# Here indentation is not maintained 
a = 33
b = 200
if b > a:
  print("b is greater than a") # you will get an error


# Elif logic
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# else logic
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# else logic without elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

if a > b: print("a is greater than b")


# Short Hand If ... Else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

a = 2
b = 330
print("A") if a > b else print("B")


# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


# logical operator (and)
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


# logical operator (or)
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# logical operator not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


# Nested if

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


#pass statement

a = 33
b = 200

if b > a:
  pass


