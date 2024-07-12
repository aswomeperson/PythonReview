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
  """
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