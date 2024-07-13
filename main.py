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
'''
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

    