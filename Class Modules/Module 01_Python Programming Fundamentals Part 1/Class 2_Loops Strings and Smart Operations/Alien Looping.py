# For Loops
print("🍩 Sunny is testing the donut dispenser...")

donuts = ["glazed", "chocolate", "galactic sprinkle", "neutron nut"]
for donut in donuts:
    print("Dispensing", donut, "donut!")

print()

# While Loops
print("🌀 Sunny enters a loop to find the right launch angle...")

angle = 0
while angle < 90:
    print("Testing angle:", angle)
    angle += 30

print("✅ Found a good launch angle!\n")

# Break & Continue
print("🤖 Sunny tests launch protocols, skipping bad ones:")

protocols = ["ok", "ok", "bad", "ok", "bad", "ok"]

for i, p in enumerate(protocols):
    if p == "bad":
        print("⚠️ Protocol", i, "is bad, skipping!")
        continue
    print("✅ Protocol", i, "is good.")

print("🛑 But wait, one protocol self-destructed!")
for i, p in enumerate(protocols):
    if p == "bad":
        print("💥 Protocol", i, "failed badly! ABORT MISSION!")
        break
    print("Running Protocol", i)

print("\n🛸 Sunny learned a lot and returned home... with loops in his brain forever!")



for pod in range(5):
    print("🧹 Cleaning pod number", pod)


for label in range(1, 6):
    print(f"📦 Box {label} labeled and loaded")


for pod in range(1, 20, 3):
    print("🔢 Checking pod", pod)


for second in range(10, 0, -1):  # From 10 to 1
    print("⏳ T-minus", second)

print("🚀 Liftoff!")
