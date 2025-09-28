# 🎭 Title: “The OOP Family Saga”
# 👨 Characters:
# Mr. Object – The Dad (Husband)

# Mrs. Classy – The Mom (Wife)

# Inno – The Nerdy Son

# Multi – The Clever Daughter

# Grandpa OOP – The wise old man (Pops in randomly)


# ☕ Scene 1: Introduction at the Breakfast Table
# Narrator:
# Welcome to the OOP family – 
# where everything is structured, yet chaotic like real code! Meet Mr. Object and his wife Mrs. Classy, and their brilliant kids, Inno and Multi.

# ☕ Script:
# Mr. Object:
# “Classy, these kids keep inheriting all my habits, good or bad!”

# Mrs. Classy:
# “That’s called Single Inheritance, dear. Inno got your laziness and your love for coffee.”

# ✅ Topic: Single Inheritance
# One class (child) inherits from one parent class.


class Father:
    def skills(self):
        print("I can code in C++")

class Son(Father):
    pass

inno = Son()
inno.skills()  # Output: I can code in C++


# 👨‍👩‍👧 Scene 2: Sibling Shenanigans
# Inno:
# “I also got Mom’s cooking skills! But Multi got her shopping addiction!”

# ✅ Topic: Hierarchical Inheritance
# Multiple children inherit from one parent.


class Mom:
    def cooking(self):
        print("Cooking delicious biryani")

class Inno(Mom):
    pass

class Multi(Mom):
    pass

inno = Inno()
multi = Multi()
inno.cooking()
multi.cooking()



# 🧗 Scene 3: The Family Tree
# Multi:
# “I’m learning from Inno now. He’s teaching me how to code!”

# ✅ Topic: Multilevel Inheritance
# A child inherits from a parent, and then another class inherits from that child.


class Grandpa:
    def advice(self):
        print("Never ignore bugs!")

class Father(Grandpa):
    def teach(self):
        print("Teaching Java")

class Son(Father):
    pass

multi = Son()
multi.advice()
multi.teach()


# 🧬 Scene 4: The Confused Genius
# Mrs. Classy:
# “But how did Multi also learn from Uncle Logic? She’s everywhere!”

# ✅ Topic: Multiple Inheritance
# One child inherits from multiple parents.

class Mother:
    def discipline(self):
        print("Go to bed at 10!")

class UncleLogic:
    def math(self):
        print("Solving equations...")

class Daughter(Mother, UncleLogic):
    pass

multi = Daughter()
multi.discipline()
multi.math()


# 🎯 Scene 5: The Overloaded Phone Call
# Inno (on phone):
# “Hello Dad! Oh, you want to know my marks?
# Oh, and Mom’s asking for my marks in each subject?”

# ✅ Topic: Method Overloading (simulated in Python)
# Same method name, different arguments. (Python doesn’t support true overloading but we simulate it.)


class ReportCard:
    def marks(self, math=None, english=None):
        if math is not None and english is not None:
            print(f"Math: {math}, English: {english}")
        elif math is not None:
            print(f"Math: {math}")
        else:
            print("No marks given.")

inno_report = ReportCard()
inno_report.marks(90)
inno_report.marks(90, 85)


# 🥊 Scene 6: The Override Battle
# Mr. Object:
# “I’m the head of this family!”

# Multi:
# “In your dreams! I’m the CEO of our Instagram business!”

# ✅ Topic: Method Overriding

class Parent:
    def role(self):
        print("I’m the boss!")

class Child(Parent):
    def role(self):
        print("I run the show now!")

multi = Child()
multi.role()  # Output: I run the show now!



# 🔒 Scene 7: Secrets in the Family
# Narrator:
# Mr. Object has a secret fund… but no one knows the variable name.

# ✅ Topic: Encapsulation


class Family:
    def __init__(self):
        self.__secret_fund = 5000  # private variable

    def get_fund(self):
        return self.__secret_fund

dad = Family()
print(dad.get_fund())
# print(dad.__secret_fund)  # ❌ Will raise an error





# 🐙 Scene 8: Shape-shifting Mom
# Mrs. Classy (on call):
# “I’m a cook, a doctor, a teacher, and a detective—all depending on the situation!”

# ✅ Topic: Polymorphism
class Role:
    def act(self):
        pass

class Cook(Role):
    def act(self):
        print("Cooking dinner...")

class Doctor(Role):
    def act(self):
        print("Prescribing medicine...")

def daily_roles(role):
    role.act()

daily_roles(Cook())
daily_roles(Doctor())


