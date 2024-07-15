import pandas as pd 
'''
x = 5
y = "Hello World CHAT"

if x > 2:
  print(y)

# Beginner Stuff doing again- Refreshing my MEMORY

Name = "John"
Woman_Name = "Mary"
print(Name + " and " + Woman_Name + " are Sisters")

x = str(3)
x = int(4)
x = float(3)
print(type(x))

names = ["John", "Rajesh", "Lina"]
x, y, z = names
print(x, y, z)

def testfunction():
  global rc
  rc = "jajajajajajja"
  x, y, z = "Timmeh", "Guapo", "Rodrigo"
  print(x, y, z + " are Tom's Friends!", rc )

testfunction()
print(x, y, z + "Are toms friends!", rc )

# Common Name Generator
# with only 4 premade names
names = ["Dave", "Ragreh", "Jimmy","Timmy"]
a = b = c = d = names 
random_num = input("Enter a Number to get your premade name(0-4):")
x = int(random_num)
print(names[0+x])

def main():
  print("This is text coming from the main function of the program!")
  secondary_function()

def secondary_function():
  print("This is text coming from the secondary function of the program!")

if __name__ == '__main__':
  main()

# Python Operators/Calculator
basic = float(input("Enter a number:"))
basic2 = float(input("Enter 2nd number:"))
logic = input("Add Operator(+,-,*,/):")
if logic == "+":
  print(basic + basic2)
elif logic == "-":
  print(basic - basic2)
elif logic == "*":
  print(basic * basic2)
elif logic == "/": 
  print(basic/basic2)
elif basic2 == 0 and basic == 0 and logic == "/":
  print("Error. Please Restart Program FOOL")
else:
  print("Please put in a valid operator! (+,-,*,/)")
  logic = input("Add Operator(+,-,*,/):")
print(logic)


global name
name = input("Welcome, before we can EVEN start, what is your name? ")
print("Great! Nice to meet you", name)

# Introduction function
def intro():
    print("Welcome to the Wild Adventure of Ricky the RAT!\n")
    print("You are a rat, and you are trying to get to the end of the world. You are currently trying to escape mysterious monsters that look like hairless monkeys. Humans! That's what they call themselves, well either way, you are a rat, so you want to steal as much cheese, but NOT get caught by them. Understand? Great!\n")
intro()

def choice1():
    global condition
    c1 = input("You are in Gizmo's kitchen and see Gizmo, faced away from you watching TV. Will you run to the kitchen to look for cheese, or will you go try to interact and watch TV with him? (run/watch) \n")
    if c1 == "run":
        print("You run to the kitchen to quickly grimace and look for food but it takes time... \n")
        condition = 0
    elif c1 == "watch":
        print("You go and try to watch TV with Gizmo, clearly interested in whatever he is doing but he sees you and jumps in fear. 'AHhhhh!' He grabs his shotgun and shoots you, but he missed! You run and scamper off... \n")
        condition = 1
choice1()

def choice2():
    global condition
    if condition == 0:
        c1 = input("Yes! You finally find FOOD. However, one food is poisoned and the other is not. The catch? You don't know which one is poisoned. Choose one: (left/right) \n ")
        if c1 == "left":
            print("You chose the left food. Luckily, it was not poisoned! You continue your adventure. \n")
            condition = 2
        elif c1 == "right":
            print("You chose the right food. Unfortunately, it was poisoned. Game over. \n")
    elif condition == 1:
        c2 = input("You run, but Gizmo catches up to you until you are cornered. You realize that there is no escape so you only have a option to fight. You see salt next to you and realize you can blow the dust into his eyes and mouth, temporarily restraining him. You look to your right and see a knife. What will you use? (knife/salt) \n")
        if c2 == "knife":
            print("You grab the knife that is 10 times bigger than you and charge at Gizmo, like a true warrior. You imagine defeating him as victory comes closer to you. Oh yeah I forgot to mention the catch- you NEVER bring a knife to a gunfight. As soon as you're in range he clicks the trigger and you are vaporized. I would have said 'Game Over' but I'm in Shock. \n")
        elif c2 == "salt":
            print("You grab the salt and throw it at Gizmo's eyes and mouth. He is confused for a second but then the pain hits him. Then you attack him so badly I can't even describe it. You Won - THE VICIOUS ENDING \n")
choice2()

# The LAST choice
def choice3():
    global condition
    if condition == 2:
        c1 = input("As you walk off, you can see the door in the distance! Yes, you might be able to get out of here, but as soon as you are about to reach the door, you see a monster with 4 legs, a tail, and a head. It looks like a cat! You see that there is no other way of leaving so this is it. You either win or lose. The cat says to you 'I will let you go if you can answer my riddle. If you get it wrong, you will be my meal!'. \nI am both vast and wide\nHome to stars that may have died\nDark and light, and full of might\nHolding galaxies in my sight. (universe/multiverse) \n")
        if c1 == "universe":
            print("Correct! Hmm, you are smart for a rat. Keep up the work. You then walk off into the distance. You Win! THE TRUE ENDING")
        elif c1 == "multiverse":
            print("Right but wrong. You are a rat. You are a rat. The cat then eats you. Welp that was a sad ending. GAME OVER")
choice3()

#Loops
for KAD in range(5):
    print(KAD)

BIG_C = 0
while BIG_C < 5:
    print(BIG_C)
    BIG_C+=1
BIG_C = 0
#TWO WAYS TO DO IT
while True:
    print(BIG_C)
    BIG_C+=1
    if BIG_C >= 5:
        break 

#NESTED LOOPS REFRESH
for i in range(3):
  for j in range(2):
    print(f"i: {i}, j: {j}")
#LIST MINI PROJECT
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(squares) 
#FUNCTION PROJECT
def sum_even_numbers(numbers):
  total = 0
  for num in numbers:
    if num % 2 == 0:
      total += num
  return total
my_numbers = [1, 4, 7, 2, 9, 6]
result = sum_even_numbers(my_numbers)
print("Sum of even numbers:", result)

#GUESSING PROJECT
secret_num = 7
guess = 3
while guess > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_num:
        print("You guessed it!")
        break
    elif guess < secret_num:
        print("Too low!")
    elif guess > secret_num:
        print("Too high!")
    guess -= 1
    if guess > 10:
        print("Sorry But Thats TOO HIGH")
if guess == 0:
    print("YOU LOST!!!!")

for ra in range(10):
    if ra == 5:
        break
    print(ra)
    if ra == 2:
        continue
    print(ra)
    if ra == 7:
        pass
    print(ra)
        
def treasurechest():

  print("Welcome to the Mystery CAGE!")
  items = ["gold coin", "rusty key", "empty box", "magic potion", "dragon egg"]
  for i in range(len(items)):
    print(f"Item {i+1}:")
    item = items[i]
    if item == "dragon egg":
      print("Whoa! You found a dragon egg! This is too valuable, I'll keep it safe heheh...")
      break  #this will stop the loop
    elif item == "empty box":
      print("This is disappointing. You got nothing.")
      continue  # Skip to THE NEXT ITEM
    elif item == "rusty key":
      print("You found a key! You should probably clean it.")
      pass  
    else:
      print(f"You found a {item}! It's yours to keep.")

treasurechest()

def average(number):
    if not number:
        return 0  # Return 0 if the list is empty
    total = sum(number)
    avg = total / len(number)
    return avg  # Return the average

num_str = input("Enter a list of numbers separated by spaces to get the average: ")
number = [float(num) for num in num_str.split()]

try:
    avg = average(number)
    print("The average of the entire list is:", avg)
except ZeroDivisionError:
    print("Cannot compute the average of an empty list.")
except ValueError:
    print("Please enter valid numbers only.")
finally:
    print("This is the final statement")
#functions
#Simple Addidition Function

def addnums(num1,num2,num3):
    sum = num1+num2+num3
    print(sum) 
addnums(1,2,3)

#lang function
def greetings(lan):
    var = lan.lower()
    if var == "spanish":
        print("Hola! Como Estas?")
    elif var == "french":
        print("Bonjur!")
    elif lan == "chinese":
        print("Ni hao!")

    elif var == "English":
        print("HOWDY FELLA! HOW YOU DOING?")
    else:
        print("Hmm, sorry I only know Spanish, French, Chinese, and English!")

greetings("spanish")
#Ackerman Function
def ackermann(m, n, indent=None):
    if indent is None:
        indent = 0
    print(f"{' ' * indent} Ackermann ({m}, {n})")

    if m == 0: 
        return n + 1
    elif m > 0 and n == 0:  
        return ackermann(m - 1, 1, indent + 1)
    elif m > 0 and n > 0:  
        return ackermann(m - 1, ackermann(m, n - 1, indent + 1), indent + 1)

print("Starting with m = 1, n = 1:")
print(ackermann(1, 1))

print("Starting with m = 2, n = 3:")
print(ackermann(2, 3))


#TO DO: MAKE A FACTORIAL FUNCITON

#recursion 
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

reversed_str = reverse_string("ARCADE HACKATHON")
print(f"Reversed string: {reversed_str}")
#GCD Calculator
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(a, a%b)
result = gcd(2, 4)
print(result)   

def addlist(rst):
    if len(rst) == 0:
        return 0
        #because if a list has 0 in it, it must return 0 right?
    else:
        return rst[0] + addlist(rst[1:]) #Starts from the first number [0] and recursivly calls each other one via rst[1:]

examplelist = [2,4,100,92222]

sum = addlist(examplelist)
print("The sum is:", sum)

def pali(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and pali(s[1:-1])

result = pali("KADU")
print("Is it  a palindrome?",result)
#find the power somehing
def power(base, exponent):
    if exponent == 0:
        return 1
        #bcz something to the power of 0 always is 1
    elif exponent % 2 == 0:
        return power(base, exponent // 2) ** 2
    else:
        return base * power(base, exponent - 1)

base_num = 2
exp = 5
result = power(base_num, exp)
print(base_num, "to the the power of", exp, "equals to",result)


#simple factorial 
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
        
print("the Factorial is",factorial(3))

#Project: Mad Libs

def madlibs(temp):
    if "(Noun)" in temp:
        noun = input("Enter a propper noun for the madlib: \n")
        temp = temp.replace("(Noun)", noun, 1) # So only first time noun come- u replace
    if "(Adjective)" in temp:
        adjective = input("Enter a adjective for the madlib: \n")
        temp = temp.replace("(Adjective)", adjective, 1)
    if "(Verb)" in temp:
        verb = input("Enter a verb ending in ing for the madlib: \n")
        temp = temp.replace("(Verb)",verb,1)
    #check if everything in the base template is REPLACED
    if "(Noun)" not in temp and "(Adjective)" not in temp and "(Verb)" not in temp:
        return temp

exampletemp = "Once upon a time,(Noun) lived hapily in a (Adjective) forest. \n One day a intruder came and so they said its (Verb) time!"

story = madlibs(exampletemp)
print(story)

#Lambda Functions And Importing
add = [1, 2, 3, 4, 5, 6]
new_add = list(map(lambda x: x * 2, add))
print(add) 
#Make a grading system and change the scores project
school = pd.DataFrame({
    'name':['TIMMEH','RAJESH','KADU','Billy','Raj'],
    'scores': [29,49,99,48]
})
double = [0, 4, 8, 12, 16]
value = [(lambda x: 'odd' if x % 2 else 'even')(x) for x in double]
print(value) 
#Using Pandas Librarry to create a data frame
#calling the variable and going into the scores part of it: df[scores]. By doing this when we return or print df it will update the scores like this. This is useful because if you dont want to edit the code in the function itself you can use it like this
school['scores'] = school['scores'].apply(lambda y: y* 2)
print(school)
#edited JUST the scores part of it by 2
'''
#Objects, classes 

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        if self.species.lower() == "dog":
            return "BARK BARK!"
        elif self.species.lower() == "cat":
            return "HISS HISS!"
        else:
            return "bro idk what to play here"

# Creating objects of the Pet class
my_dog = Pet(name="Buddy", species="Dog")
my_cat = Pet(name="Whiskers", species="Cat")

# Use the objects
print(f"{my_dog.name} says: {my_dog.make_sound()}")
print(f"{my_cat.name} says: {my_cat.make_sound()}")

#trying to make a library mini project

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book (self, book):
        self.books.append(book)
#need help on this part of the code
    def borrow_book(self, debook_tittle):
        for book in self.books:
            if book.title == book_title and book.available:
                book.davailable = False
                print(f"{book.title} borrowed.")
                return
        print(f"Book '{book_title}' not found or TAKEN HAHAHA.")

    def return_book(self, book_title:
        for book in self.books:
            if book.title == book_title and not book.available:
                book.available = True
                print(f"book.title} returned")
                return
        print(f"Book '{book_title}' not found or already returned.")

    def display_books(self):
        print("Books allowed:")
        for book in self.books:
            if book.available=
                print(f"- {book.title} by {book.author}")
