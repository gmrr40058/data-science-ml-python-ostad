import math

distance_to_home = 384400  # in km (distance to moon for fun)
# Math Functions
print("🔭 Sunny checks Earth’s gravitational pull to adjust thrust.")
gravity = 9.8
thrust_needed = math.sqrt(gravity * distance_to_home)
print("Thrust Needed:", round(thrust_needed, 2), "Sunny-Newtons\n")

print("\n🗿 Sunny builds a perfect pyramid using Math Module")

base_length = 10
height = 15

# Area of triangle formula: 0.5 * base * height
area = 0.5 * base_length * height
print("Area of triangular wall:", area)

# Sunny wants to know the hypotenuse of the side
hypotenuse = math.sqrt(base_length**2 + height**2)
print("Slanted side (hypotenuse):", round(hypotenuse, 2))

# Calculate sin of the angle for fun
angle_radians = math.atan(height / base_length)
angle_degrees = math.degrees(angle_radians)
print("Launch angle:", round(angle_degrees, 2), "degrees")

# Sunny decides to round to nearest integer
print("Rounded angle:", round(angle_degrees))

carrots_exact = 5.87  # Sunny counted with his weird scanner

# Round up to nearest whole carrot
carrots_up = math.ceil(carrots_exact)
print("🥕 Carrots (rounded up):", carrots_up)

# Round down to nearest whole carrot
carrots_down = math.floor(carrots_exact)
print("🥕 Carrots (rounded down):", carrots_down)
