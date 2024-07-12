"""x = 5
y = "Hello World CHAT"

if x > 2:
  print(y)

#Beginner Stuff doing again- Refreshing my MEMORY

Name = "John"

Woman_Name = "Mary"

print(Name + " and " + Woman_Name + " are Sisters")

x = str(3)

x = int(4)

x = float(3)

print(type(x))

names = ["John", "Rajesh", "Lina"]
x,y,z = names

print(x,y,z)

def testfunction():
  global rc
  rc = "jajajajajajja"
  x,y,z = "Timmeh", "Guapo", "Rodrigo"
  print(x,y,z + " are Tom's Friends!", rc )

testfunction()
print(x,y,z + "Are toms friends!", rc )

#Common Name Generator
#with only 4 premade names
names = ["Dave", "Ragreh", "Jimmy","Timmy"]
a = b = c = d = names 
random_num = input("Enter a Number to get your premade name(0-4):")
x = int(random_num)
print(names[0+x])
#simple basic stuff esentially

def main():
  print("This is text coming from the main function of the program!")
  secondary_function()

def secondary_function():
  print("This is text coming from the secondary function of the program!")

if __name__ == '__main__':
  main()

#Python Operators/Calculator
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
"""
#Story Game
ascii_art = r"""
(\,/)
                            oo   '''//,        _
                          ,/_;~,        \,    / '
           ikas           "'   \    (    \    !
                                ',|  \    |__.'
                                '~  '~----''
"""
print(ascii_art)
global name
name = input("Welcome, before we can EVEN start, what is your name?")
print("Great! Nice to meet you",name)

def intro():
  print("Welcome to the Wild Adventure of Ricky the RAT!")
  print("You are a rat, and you are trying to get to the end of the world. You are currently trying to escape mysterious monsters that look like hairless monkeys. Humans! That's what they call themselves, well either way, you are a rat, so you want to steal as much cheese, but NOT get cought by them. Understand? Great!")
intro()

def choice1():
  c1 = input("You are in Gizmo's kitchen and see Gizmo, faced away from you watching TV. Will you run to the kitchen to look for cheese, or will you go try to interact and watch tv with him? (run/watch)")
  
  if c1 == "run":
    print("You run to the kitchen to quickly grimace and look for food but it takes time...")
    global condition
    condition = 0
  elif c1 == "watch":
    print("You go and try to watch TV with Gizmo, clearly interested in whatever he is doing but he sees you and jumps in fear. 'AHhhhh!' He grabs his shotgun and shoots you, but he missed! You run and scamper off...")
    condition = 1
choice1()
def choice2():
  if condition == 0:
    c1 = input == "Yes! You finnaly find FOOD. However, one food is poisoned and the other is not. The Catch? You don't know what is posioned,",name, "The two food"
choice2()
#loops