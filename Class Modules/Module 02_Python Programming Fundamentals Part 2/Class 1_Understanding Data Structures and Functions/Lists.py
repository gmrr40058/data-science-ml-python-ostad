# Story Outline:
# Once upon a time in the magical land of Pylandia, a bunch of data structures threw a party.

# Lists were the cool kids who loved to collect everything: snacks, jokes, and even exes.

# Dictionaries were the classy ones, always coming with pairs — name cards and phone numbers!

# Functions were the organizers of the party. They did all the work, especially Chef Function, who always asked for parameters like "ingredient" or "dish_type".

# Sometimes, Chef Function would get moody if you didn't pass the right arguments — unless he had default values ready, like pizza 🍕!

# They all had to go home at midnight, so they shouted return "BYE" and vanished!

# The list guy walks in with: ["Chips", "Soda", "Cake"]


snacks = ["Chips", "Soda", "Cake"]
print("Snacks:", snacks)

snacks.append("Cookies")
print("After adding Cookies:", snacks)

snacks.remove("Soda")
print("Soda was too fizzy. Removed:", snacks)

snacks.sort()
print("Snacks in alphabetical order:", snacks)



# Imagine a row of party snacks. You want the first snack.

snacks = ["Chips", "Cake", "Soda", "Pizza"]
print("First snack:", snacks[0])   # Chips
print("Last snack:", snacks[-1])   # Pizza

# Someone stole the Soda. You replace it with Juice.
snacks[2] = "Juice"
print("After replacement:", snacks)


# Someone brought Cookies — insert it before Cake!
snacks.insert(1, "Cookies")
print("After inserting Cookies:", snacks)



# Pizza was cold. Kick it out!
del snacks[4]
print("After deleting Pizza:", snacks)


# Pop the last item, like a surprise!
last_snack = snacks.pop()
print("Popped:", last_snack)
print("Remaining snacks:", snacks)


# Party's over — clean the snack table.
snacks.clear()
print("After clearing:", snacks)


# List of guests, each bringing a list of items.
party_bags = [
    ["Chips", "Cookies"],
    ["Cake", "Juice"],
    ["Soda", "Pizza"]
]

for bag in party_bags:
    for item in bag:
        print("Bag has:", item)


# Two snack tables merge like Avengers Assemble!
table1 = ["Chips", "Juice"]
table2 = ["Cake", "Cookies"]

full_table = table1 + table2
print("Combined Table:", full_table)





