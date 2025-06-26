#CODE FOR PROJECT WITH A SEARCH METHOD, SO USER CAN DOWNLOAD THE FILES(JUST MAIN.PY) 


def unit1():
    # beginner stuff doing again- refreshing my memory

    name = "john"
    woman_name = "mary"
    print(name + " and " + woman_name + " are sisters")

    x = str(4)
    x = int(4)
    x = float(
    #new change
        
        
        
        3)
    print(type(x))

    names = ["john", "rajesh", "lina"]
    x, y, z = names
    print(x, y, z)

    # common name generator
    # with only 4 premade names
    names = ["dave", "ragreh", "jimmy", "timmy"]
    random_num = input("enter a number to get your premade name(0-3):")
    x = int(random_num)
    print(names[x])

    # python operators/calculator
    basic = float(input("enter a number:"))
    basic2 = float(input("enter 2nd number:"))
    logic = input("add operator(+,-,*,/):")
    if logic == "+":
        print(basic + basic2)
    elif logic == "-":
        print(basic - basic2)
    elif logic == "*":
        print(basic * basic2)
    elif logic == "/":
        if basic2 != 0:
            print(basic / basic2)
        else:
            print("error. division by zero")
    else:
        print("please put in a valid operator! (+,-,*,/)")
        logic = input("add operator(+,-,*,/):")
        if logic == "+":
            print(basic + basic2)
        elif logic == "-":
            print(basic - basic2)
        elif logic == "*":
            print(basic * basic2)
        elif logic == "/":
            if basic2 != 0:
                print(basic / basic2)
            else:
                print("error. division by zero")
    print(logic)

def unit2():
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
        else:
            print("Choose the two options!")
            choice1()
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
            else:
                print("Choose the two options!")
                choice2()
        elif condition == 1:
            c2 = input("You run, but Gizmo catches up to you until you are cornered. You realize that there is no escape so you only have a option to fight. You see salt next to you and realize you can blow the dust into his eyes and mouth, temporarily restraining him. You look to your right and see a knife. What will you use? (knife/salt) \n")
            if c2 == "knife":
                print("You grab the knife that is 10 times bigger than you and charge at Gizmo, like a true warrior. You imagine defeating him as victory comes closer to you. Oh yeah I forgot to mention the catch- you NEVER bring a knife to a gunfight. As soon as you're in range he clicks the trigger and you are vaporized. I would have said 'Game Over' but I'm in Shock. \n")
            elif c2 == "salt":
                print("You grab the salt and throw it at Gizmo's eyes and mouth. He is confused for a second but then the pain hits him. Then you attack him so badly I can't even describe it. You Won - THE VICIOUS ENDING \n")
            else:
                print("Choose the two options!")
                choice2()
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

    # Loops
    for KAD in range(5):
        print(KAD)

    BIG_C = 0
    while BIG_C < 5:
        print(BIG_C)
        BIG_C += 1
    BIG_C = 0

    # TWO WAYS TO DO IT
    while True:
        print(BIG_C)
        BIG_C += 1
        if BIG_C >= 5:
            break

def unit3():
    def treasurechest():
        print("Welcome to the Mystery CAGE!")
        items = ["gold coin", "rusty key", "empty box", "magic potion", "dragon egg"]
        for i in range(len(items)):
            print(f"Item {i+1}:")
            item = items[i]
            if item == "dragon egg":
                print("Whoa! You found a dragon egg! This is too valuable, I'll keep it safe heheh...")
                break  # this will stop the loop
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

    # Simple Addition Function
    def addnums(num1, num2, num3):
        sum = num1 + num2 + num3
        print(sum) 

    addnums(1, 2, 3)

    # Language function
    def greetings(lan):
        var = lan.lower()
        if var == "spanish":
            print("Hola! Como Estas?")
        elif var == "french":
            print("Bonjur!")
        elif lan == "chinese":
            print("Ni hao!")
        elif var == "english":
            print("HOWDY FELLA! HOW YOU DOING?")
        else:
            print("Hmm, sorry I only know Spanish, French, Chinese, and English!")

    greetings("spanish")

    # Ackermann Function
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

    # Recursion 
    def reverse_string(s):
        if len(s) == 0:
            return s
        else:
            return reverse_string(s[1:]) + s[0]

    reversed_str = reverse_string("ARCADE HACKATHON")
    print(f"Reversed string: {reversed_str}")

    # GCD Calculator
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)

    result = gcd(2, 4)
    print(result)   

    def addlist(rst):
        if len(rst) == 0:
            return 0
        else:
            return rst[0] + addlist(rst[1:])

    examplelist = [2, 4, 100, 92222]
    sum = addlist(examplelist)
    print("The sum is:", sum)

    def pali(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and pali(s[1:-1])

    result = pali("KADU")
    print("Is it a palindrome?", result)

    # Power function
    def power(base, exponent):
        if exponent == 0:
            return 1
        elif exponent % 2 == 0:
            return power(base, exponent // 2) ** 2
        else:
            return base * power(base, exponent - 1)

    base_num = 2
    exp = 5
    result = power(base_num, exp)
    print(base_num, "to the power of", exp, "equals to", result)

    # Simple factorial 
    def factorial(num):
        if num == 0:
            return 1
        
        else:
            return num * factorial(num - 1)

    print("The factorial is", factorial(3))




def unit4():
    # Mad Libs Project
    def madlibs(temp):
        while "(Noun)" in temp:
            noun = input("Enter a proper noun for the madlib: \n")
            temp = temp.replace("(Noun)", noun, 1)
        while "(Adjective)" in temp:
            adjective = input("Enter an adjective for the madlib: \n")
            temp = temp.replace("(Adjective)", adjective, 1)
        while "(Verb)" in temp:
            verb = input("Enter a verb ending in -ing for the madlib: \n")
            temp = temp.replace("(Verb)", verb, 1)
        return temp

    exampletemp = "Once upon a time, (Noun) lived happily in a (Adjective) forest. \nOne day an intruder came and so they said it's (Verb) time!"
    story = madlibs(exampletemp)
    print(story)

    # Lambda Functions and Importing
    add = [1, 2, 3, 4, 5, 6]
    new_add = list(map(lambda x: x * 2, add))
    print(add)
    print(new_add)

    # Make a grading system and change the scores project
    school = {
        'name': ['TIMMEH', 'RAJESH', 'KADU', 'Billy', 'Raj'],
        'scores': [29, 49, 99, 48]
    }
    double = [0, 4, 8, 12, 16]
    value = ['odd' if x % 2 else 'even' for x in double]
    print(value)

    school['scores'] = [score * 2 for score in school['scores']]
    print(school)

    # Objects, classes
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

        def make_name(self):
            if self.name.lower() == "buddy":
                return "Buddy? That's a cool name"
            elif self.name.lower() == "whiskers":
                return "Whiskers? Now that's a name I haven't heard in a long time...."
            else:
                return f"Well, I'm not sure what your name means, {self.name}"

    my_dog = Pet(name="Buddy", species="Dog")
    my_cat = Pet(name="Whiskers", species="Cat")

    # Use the objects
    print(f"{my_dog.name} says: {my_dog.make_sound()}")
    print(f"{my_cat.make_name()}. What do you say {my_cat.name}? {my_cat.make_sound()}")

    # Library mini project
    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author
            self.available = True

    class Library:
        def __init__(self):
            self.books = []

        def add_book(self, book):
            self.books.append(book)

        def borrow_book(self, book_title):
            for book in self.books:
                if book.title == book_title and book.available:
                    book.available = False
                    print(f"{book.title} borrowed successfully.")
                    return
            print(f"Book '{book_title}' not found or already borrowed.")

        def return_book(self, book_title):
            for book in self.books:
                if book.title == book_title and not book.available:
                    book.available = True
                    print(f"{book.title} returned successfully.")
                    return
            print(f"Book '{book_title}' not found or already returned.")

        def display_books(self):
            print("Available books:")
            for book in self.books:
                if book.available:
                    print(f"- {book.title} by {book.author}")

    my_library = Library()
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.display_books()
    my_library.borrow_book("1984")
    my_library.display_books()
    my_library.return_book("1984")
    my_library.display_books()

def unit5():
    # Simple auth class
    class User:
        def __init__(self, user, password, info):
            self.user = user
            self.password = password
            self.info = info
            self.verified = False

        def verify_user(self):
            if self.user == "KADU" and self.password == "HelloWorld123":
                print(f"{self.user} has now logged in. Welcome Back!")
                self.verified = True
            elif self.user == "Jimmy123" and self.password == "CrazyJim1992":
                print(f"{self.user} has now logged in. Welcome Back!")
                self.verified = True
            else:
                print(f"{self.user} or {self.password} is not a valid username or password. Please try again")

        def give_info(self):
            if self.verified:
                print(f"Here is your info, {self.user}: {self.info} \n")
            elif not self.info:
                print("Please provide some info about yourself!")
            else:
                print("Error 405. Hacking Detected")

        def __str__(self):
            return f"User: {self.user}\nInfo: {self.info}"

    # Example of using this class.
    user_1 = User("KADU", "HelloWorld123", "Served In Viet War. Helped People across the world. Also a proud owner of a furball named Whiskers :)")
    user_2 = User("Jimmy123", "CrazyJim1992", "Hey! My name's Jimmy! I'm currently a 24-year-old man working at McDonald's because I didn't get into a certain college. I also own a dog named Buddy!")

    print(user_1)
    print(user_2)

    # Constructors and Deconstructors
    class Colledge:
        def __init__(self, course):
            self.course = course
            print(course)

        def __del__(self):
            print('Removing Your College Class')

    # Create a Colledge class object
    sched = Colledge('COLLEGE CLASS OF COMPUTER SCIENCE!')
    # Delete the Colledge class object
    del sched

    # Project on foundations of a building
    class BuildingFoundation:
        def __init__(self, material):
            self.material = material  # Can be accessed outside of the class
            self.strength = 100
            self.blueprint = []
            self._secret = "This is a secret message...."  # Cannot be accessed outside because of "_"

        def reinforce(self, additional_strength):
            self.strength += additional_strength

        def deconstruct(self):
            self.strength -= 20
            if self.strength < 0:
                print("Warning: Building MIGHT FALL. CODE RED")

        def add_blueprint(self, component):
            self.blueprint.append(component)

        def build(self):
            if self.strength >= 80 and self.blueprint:
                print(f"Making a {self.material} skyscraper!")
                print("Components:")
                for component in self.blueprint:
                    print(f" - {component}")
            else:
                print("Not enough strength or missing blueprint components. Reinforce or plan first.")

    # Declare old_foundation
    old_foundation = BuildingFoundation("Monkey Soil")
    # Reinforce
    old_foundation.reinforce(additional_strength=30)
    # Add blueprint
    old_foundation.add_blueprint("Elevator")
    old_foundation.add_blueprint("Water Fountain")
    old_foundation.add_blueprint("Green rooftop bar and restaurant")
    # Deconstruct
    old_foundation.deconstruct()
    # Now build
    old_foundation.build()

    # Access Modifications
    new_foundation = BuildingFoundation("Galvanized Metal Pipes")  # Initialize the function
    print(new_foundation.material)  # Accessing the material of the Foundation class outside of the class

def unit6():
    # Car mini project
    class Car:
        def __init__(self, car, seating):
            self.car = car  # Public object
            self._mileage = 0  # Private object
            self.__fuel_level = 100  # Private object

        def drive(self, distance):
            self._mileage += distance
            print(f"Driven {distance} miles. Total mileage: {self._mileage}")

        def refuel(self, amount):
            self.__fuel_level += amount
            print(f"Refueled by {amount} units. Fuel level: {self.__fuel_level}%")

        def __del__(self):
            print("Car object destroyed.")

    # Example usage:
    model_3 = Car("Sedan", 5)
    model_3.drive(50)
    model_3.refuel(20)

    # Encapsulation
    class InfoUser:
        def __init__(self, user, email):
            self.user = user
            self.email = email

        def check_username(self, username_to_check):
            return username_to_check == self.user

    user = InfoUser('user1212', 'jaja@gmil.i')

    print(user.check_username('user1212'))  # returns True
    print(user.check_username('useerrrrrrr'))  # returns False

    class BankAccount:
        def __init__(self, account, starting_balance):
            self.account = account
            self.starting_balance = starting_balance

        def deposit(self, amount):
            if amount > 0:
                self.starting_balance += amount
                print(f"Gave ${amount}. New balance: ${self.starting_balance}")
            else:
                print("Not Valid amount.")

        def withdraw(self, amount):
            if 0 < amount <= self.starting_balance:
                self.starting_balance -= amount
                print(f"Withdrew ${amount}. New balance of money: ${self.starting_balance}")
            else:
                print("NOT ENOUGH FUNDS OR INVALID AMOUNT!!!")

        def get_balance(self):
            return self.starting_balance

    # Using it
    my_account = BankAccount("Kadu", 1000)
    print(f"Account holding: {my_account.account}")
    print(f"Starting balance: ${my_account.get_balance()}")

    my_account.deposit(200)
    my_account.withdraw(150)
    print(f"Balance: ${my_account.get_balance()}")

    # Inheritance
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def print_info(self):
            print(f"HERE IS YOUR JOB AND CAREER PERSON. NAME: {self.name} AGE: {self.age} JOB: {self.prof}")

    class Job(Person):
        def __init__(self, name, age, prof):
            super().__init__(name, age)
            self.prof = prof

        def random_job(self):
            job_titles = ["Software Engineer", "Data Scientist", "Teacher at Harvard", "Janitor at Tacobell :("]
            self.prof = job_titles[0]  # Simple selection logic

    myEpicGuy = Job("John Lather", 49, "")
    myEpicGuy.random_job()
    myEpicGuy.print_info()

    # Polymorphism, etc.
    class Animal:
        def speak(self):
            raise NotImplementedError("PUT IN THE SUBCLASS BRO!")

    class Dog(Animal):
        def speak(self):
            print("Bark BARK!")

    class Cat(Animal):
        def speak(self):
            print("HISS HISS!!!")

    dog_instance = Dog()
    cat_instance = Cat()
    # Make them say stuff
    dog_instance.speak()
    cat_instance.speak()

    class Check:
        def type(self):
            print('You have a checking account at the Royal English Arcade.')

        def balance(self):
            print('$20 left, brokie!')

    class Save:
        def type(self):
            print('You have a savings account at the Royal French Arcade')

        def balance(self):
            print('$1000 left in your savings.')

    account_a = Check()
    account_b = Save()
    # Runs the balance and type.
    for account in (account_a, account_b):
        account.type()
        account.balance()

def unit7():
    class Animal_Sounds:
        def type(self):
            raise NotImplementedError("Not in subclass")

    class Tiger(Animal_Sounds):
        def speak(self):
            return "ROARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR"

    class Lion(Animal_Sounds):
        def speak(self):
            return "Lion Roar"

    class Sheep(Animal_Sounds):
        def speak(self):
            return "Mehhhhh"

    class Cow(Animal_Sounds):
        def speak(self):
            return "Moooooo"

    class Make_Sound:
        def sound(self, animal, sound):
            if animal == "" or sound == "":
                print("Cannot put Animal or Sound as empty.")
            else:
                print(f"The {animal} goes {sound}")

    # Create all the animals
    tiger = Tiger()
    lion = Lion()
    sheep = Sheep()
    cow = Cow()

    # Make all of the animals speak
    print(tiger.speak())
    print(lion.speak())
    print(sheep.speak())
    print(cow.speak())

    # Sound
    sound = Make_Sound()
    sound.sound("Mushroom Cow", "Moooshrooooom")

    # Factorial Input
    # Not premade function
    def FactorialFunction(number):
        result = 1
        for i in range(1, number + 1):
            result *= i
            print(result)

    # RUNNING MY TESTS
    FactorialFunction(4)
    FactorialFunction(5)
    FactorialFunction(6)

    FactInput = input("Enter A Number to get factorial: ")
    FactorialFunction(int(FactInput))

class search_input:
    def __init__(self,unit_functions):
        self.unit_functions = unit_functions
    def type(self,unit_functions):
        self.unit_functions = unit_functions
    def search(self,input):
        self.input = input
        if self.input == "":
            print("Please give a valid unit. Example: unit1()")

        elif self.input.lower() == "help":
            print("unit 1 is on the basic foundations, unit 2 is on functions, objects within in it and if and else statements, unit 3 is more on arthimetic series and more.  Unit 4 is on lambda functions, classes and objects going more in depth on unit 2. Unit 5 is on constructors, deconstructors, access modifications and other ways to modify classes and functions. Unit 6 goes more into classes, polymorphism, Inheritence, Objects and other topics that are harder to rebuild foundations on. Unit 7 is just sort of on different projects, and kind of a wrap up of mostly everything. \n, Run program to run the search again. \n")
                        
        elif input in self.unit_functions:
            if input in self.unit_functions:
                print(f"Succesfully found {input}: \n")
            self.unit_functions[input]()
        else:
            print("not valid. Example( unit1() )")
units = {
    "unit1()":unit1,
    "unit2()":unit2,
    "unit3()":unit3,
    "unit4()":unit4,
    "unit5()":unit5,
    "unit6()":unit6,
    "unit7()":unit7,
}
searcher = search_input(units)
print("Welcome to the unit searcher. Type 'help' to see what each units about and also see more commands. Made this instead of traditional UI, because it looks cooler!\n")
searching = input("Enter a unit to run whats inside of it or a custom command. Starts from units that are easy stuff which progressively turns harder(units 1-7). Example: unit1() \n")

searcher.search(searching)