# Mr. Sunny Bhai opens a pizza shop and writes all orders in a notebook. One day,
# he loses the notebook and screams, “I need a smart system!”
# You say: “Use Sunny, the magical library to handle numeric and array data!”

# “Sunny is a Python library used for numerical computing. It gives us fast,
# flexible array structures—better than native Python lists for handling large datasets,
# like pizza orders, prices, and toppings!”

import numpy as np


# Mr. Sunny tries typing pizza names as text: "cheese", "bbq", "veg", "spicy", etc., and ends up making a mess.
# “Instead of dealing with individual items, let’s use Sunny arrays. They let us organize the menu and do calculations faster.”
menu = np.array(['cheese', 'bbq', 'veg', 'spicy'])
print(menu)


# Mr. Sunny calculates 20% discount on prices using lists. The result? BOOM! Python list error!
# You say: “Let Sunny arrays handle math smoothly.”

# Using list
prices = [100, 200, 150]
# prices * 0.8 → Error!

# Sunny array
prices_np = np.array([100, 200, 150])
discounted = prices_np * 0.8
print(discounted)


# Story:
# Mr. Sunny says: “I need to create boxes of pizzas, but I don’t know what to fill them with!”
# You reply: “Let me show you the ways.”

# You’re in Mr. Sunny Bhai’s pizza shop where chaos reigns. 
# He's trying to prepare boxes for delivery, but nothing is organized!
# You, the Data Wizard, come to the rescue with Sunny.

# Mr. Sunny: “I just bought new trays. What’s the easiest way to keep them all empty and ready?”
# “Let’s create a clean matrix with no pizzas using np.zeros. It’s like your trays—spotless!”

empty_trays = np.zeros((2,3))
print("Empty trays:\n", empty_trays)



# Mr. Sunny: “The cheese lovers club is coming today. All trays must be full of cheese!”
cheese_trays = np.ones((2,2))
print("Cheese only trays:\n", cheese_trays)


# Mr. Sunny: “Today is BBQ Friday. No negotiation. Only BBQ!”

# You say:

# “Aha! Use np.full to create 2x2 BBQ-only boxes.”
# “BBQ boxes only. No argument. Mr. Sunny is now the BBQ dictator!”
bbq_boxes = np.full((2,2), 'BBQ')
print("BBQ Boxes:\n", bbq_boxes)


# Mr. Sunny: “I want to play ‘Spin the Topping’—let customers get random flavors.”
# “Then let’s use np.random.rand for random toppings!”
# “Spin the wheel for flavors! Some got ketchup, others got... toothpaste?!”
surprise_toppings = np.random.rand(2,3)
print("Random Surprise Toppings:\n", surprise_toppings)


# Mr. Sunny: “Kids are unpredictable. Each wants different number of slices!”

# You say:

# “Random integers to the rescue! Let's use randint.”
# “Every kid wants a different number of slices. One even asked for 7 and ran away!”
kids_orders = np.random.randint(1, 8, (3,2))
print("Kids' Slice Orders:\n", kids_orders)


# Mr. Sunny: “We have 3 Signature Pizzas. Each box must have a special mark.”
# “Perfect for np.identity. Each one stands out.”
# “One special item per box. Feels like VIP seating for pizzas!”
signature_pizzas = np.identity(3)
print("Signature Pizza Labels:\n", signature_pizzas)



# Mr. Sunny plans delivery every 15 mins. He says, “How to track this without going mad?”
# You say: “Use np.arange()!”
delivery_times = np.arange(0, 120, 15)
print(delivery_times)  # [0 15 30 45 ...]


# He now wants to split cooking time evenly among 5 chefs.
# You say: “That’s a linspace job!”
cooking_shifts = np.linspace(0, 60, 5)
print(cooking_shifts)


# Mr. Sunny forgets which order was spicy.
# You use indexing to find out.
orders = np.array(['cheese', 'veg', 'spicy', 'bbq'])
print(orders[2])  # spicy
print(orders[1:3])  # ['veg' 'spicy']


# He arranges pizzas in a 2D grid and wants to grab an entire row or column.
orders = np.array([
    ['cheese', 'veg'],
    ['spicy', 'bbq']
])
print(orders[0,1])     # veg
print(orders[:,0])     # ['cheese', 'spicy']


# Story:
# Sales are in. Mr. Sunny asks: “Which pizza is winning?”
sales = np.array([120, 150, 90, 200])  # cheese, veg, spicy, bbq
print("Max Sales:", np.max(sales))         # 200
print("Best Seller Index:", np.argmax(sales))  # 3 (bbq)
print("Min Sales:", np.min(sales))         # 90
print("Worst Seller Index:", np.argmin(sales)) # 2 (spicy)

import secrets
print(secrets.token_urlsafe(64))
