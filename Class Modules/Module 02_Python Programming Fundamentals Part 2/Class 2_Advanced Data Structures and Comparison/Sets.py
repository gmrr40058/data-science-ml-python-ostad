# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.



# Duplicate values will be ignored:

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)


# True and 1 is considered the same value:

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)


# Add an item to a set, using the add() method:

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# Add elements from tropical into thisset:

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


# Remove "banana" by using the remove() method:

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# Remove "banana" by using the discard() method:

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)


# Remove a random item by using the pop() method:

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



# The clear() method empties the set:

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


# Join set1 and set2 into a new set:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# Join a set with a tuple:

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)


# The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# Join set1 and set2, but keep only the duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)


# Keep all items from set1 that are not in set2:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)