print("👽 Welcome to Sunny's Python Adventure!\n")

# Arithmetic Operations & Operator Precedence
print("🚀 Sunny is calculating the fuel needed for Earth return.")

distance_to_home = 384400  # in km (distance to moon for fun)
fuel_efficiency = 0.5  # Sunny's ship uses 0.5 units/km

# Operator precedence: multiplication before subtraction
fuel_needed = distance_to_home * fuel_efficiency - 1000
print("Fuel Needed:", fuel_needed, "units\n")



print("\n🍩 Sunny wants 3 chocolate and 2 sprinkle donuts. Each costs 5 and 6 credits respectively.")

chocolate = 3
sprinkle = 2
price_choco = 5
price_sprinkle = 6

total_cost = chocolate * price_choco + sprinkle * price_sprinkle
print("Total cost:", total_cost)

# Adding a donut tax of 10%
tax = total_cost * 0.10
final_cost = total_cost + tax
print("Final with tax:", final_cost)


print("\n🧮 Sunny calculates space-time donut conversion...")

# Without parentheses
result1 = 10 + 5 * 2
print("Without parentheses (10 + 5 * 2):", result1)

# With parentheses
result2 = (10 + 5) * 2
print("With parentheses ((10 + 5) * 2):", result2)

# Mixing subtraction, division, and multiplication
result3 = 100 - 20 / 4 * 5
print("100 - 20 / 4 * 5 =", result3)

# Clarify using parentheses
result4 = 100 - ((20 / 4) * 5)
print("Same with parentheses:", result4)

total_slices = 8
aliens = 3

slices_per_alien = total_slices / aliens
print("🍕 Each alien gets:", slices_per_alien, "slices (with crumbs)")


total_slices = 8
aliens = 3

full_slices = total_slices // aliens
print("🔪 Full slices per alien:", full_slices)


leftovers = total_slices % aliens
print("😮 Leftover slices:", leftovers)



asteroid_sizes = [34, 7, 108, 55, 2, 89]

# Find the smallest and biggest asteroid
smallest = min(asteroid_sizes)
largest = max(asteroid_sizes)

print("🪨 Smallest asteroid:", smallest)
print("🪨 Largest asteroid:", largest)


movement = -15  # Robot moved 15 meters backward

distance = abs(movement)
print("🤖 SunnyBot moved", distance, "meters (absolute)")


base = 3  # Base power unit
exponent = 4  # Times it's amplified

laser_power = pow(base, exponent)
print("🔋 Laser Power:", laser_power)  # 3^4 = 81
