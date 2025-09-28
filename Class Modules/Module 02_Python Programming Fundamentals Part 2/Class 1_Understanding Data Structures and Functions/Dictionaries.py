# Dictionary guest shows up with a name tag and phone number.

# A dictionary is like a phonebook at the party:
# You ask for a name, and it tells you their details!

guest = {
    "name": "Alice",
    "age": 25,
    "favorite_snack": "Cake"
}

print("Guest name:", guest["name"])
print("Favorite snack:", guest.get("favorite_snack"))

# "Alice got bored of Cake. Chips it is!"
guest["favorite_snack"] = "Chips"
print("Updated snack:", guest)

# "Now she’s giving you her phone number. Easy, Python!"
guest["phone"] = "123-456-7890"
print("Added phone number:", guest)


# Some guests don't want to reveal their age. Fair enough!
guest.pop("age")
print("After removing age:", guest)


# del is harsh — no pop, just gone!
del guest["phone"]
print("After deleting phone:", guest)


# Security breach! Guest info wiped clean!
guest.clear()
print("Party guest data wiped:", guest)


# Going through a guest’s file, reading every line like a spy.
for key, value in guest.items():
    print(f"{key.title()}: {value}")


# A party full of dictionaries — it’s like a JSON family reunion
party_guests = {
    "guest1": {"name": "Alice", "snack": "Cake"},
    "guest2": {"name": "Bob", "snack": "Chips"}
}

for guest_id, details in party_guests.items():
    print(guest_id, "->", details["name"], "loves", details["snack"])

# When each guest has their own story. Like a reality show!
guests = [
    {"name": "Ravi", "snack": "Pani Puri"},
    {"name": "Sara", "snack": "Biryani"}
]

for guest in guests:
    print(f"{guest['name']} brought {guest['snack']}")







