tweet = "Hello Earth, Sunny here reporting from Sector 9."

# Slice first 5 characters
print("Start of tweet:", tweet[:5])

# Slice last 7 characters
print("End of tweet:", tweet[-7:])

# Slice middle part
print("Sector report:", tweet[25:38])

# Skip every second letter
print("Sunny's alien code:", tweet[::2])

# Reverse the tweet
print("Backwards tweet:", tweet[::-1])


messy = "Visit##Earth!! It's#sooooo!!!green###"

# Remove unwanted hashtags and exclamations
cleaned = messy.replace("#", "").replace("!", "")
print("Clean tweet:", cleaned)

# Normalize repeated letters
tweet_fixed = cleaned.replace("sooooo", "so")
print("Normalized tweet:", tweet_fixed)

# Capitalize first letter only
print("Capitalized:", tweet_fixed.capitalize())

# Title case
# print("Title Case:", tweet_fixed.title())


planet = "Earth"
activity = "farming"
alien_name = "Sunny"

tweet = "Greetings from " + planet + "! " + alien_name + " loves " + activity + "."
print("Tweet:", tweet)



planet = "Earth"
temperature = 22.56789
weather = "mild"

report = "Planet: {}, Temp: {:.1f}°C, Weather: {}".format(planet, temperature, weather)
print("Report:", report)


distance = 384400
unit = "km"

message = f"Distance to Moon from Earth: {distance} {unit}"
print("Formatted:", message)


# Formatting float with 2 decimal places
mass = 73.4578
print(f"Moon Mass: {mass:.2f} quintillion tons")



quote = "Sunny shouted: \"This planet is too green!\"\nThen he ran away...\n\t*dramatic exit*"

print("Tweet with escape characters:")
print(quote)


# Strings
print("🧠 Sunny is trying to understand Earth greetings...")
earth_hello = "Hello, Earthling!"
Sunny_greeting = earth_hello.upper()
print("Sunny yells:", Sunny_greeting)

print("He tries to whisper it...")
print("Sunny whispers:", earth_hello.lower())

print("Then he reverses it like a space magician:")
print("🔁 Reversed:", earth_hello[::-1], "\n")

print("\n🧠 Sunny is learning how humans insult with flair...")

insult = "You fight like a dairy farmer"
print("Original:", insult)

# Convert to uppercase (shouting)
print("LOUD version:", insult.upper())

# Replace words
print("Insult Remix:", insult.replace("dairy farmer", "space hamster"))

# Count letters
print("How many 'a's in insult?", insult.count('a'))

# Split into words
words = insult.split()
print("Words in insult:", words)

# Reverse the insult
reversed_insult = insult[::-1]
print("Backwards insult:", reversed_insult)