print("Hello world")
wallet = 100
print(wallet)
print("Your wallet balance is:", wallet)
print(f"Your wallet balance is: {wallet}")
day = 24
print(f"Day of the month: {day}")

temperature = -30
print(f"Temperature is: {temperature}°C")

weight = 70.5
print(f"Weight is: {weight} kg")

print(3 + 6)

print(day + 3)
print( weight - 5.5)
print( weight * 5.5)
print( weight / 5.5)

shirt = "blue"
print(f"Shirt color is: {shirt}")

name = 'John'
print(f"Hello, {name}!")

store = "Nick's Pizza shop, the \"best in town!\""
print(f"Welcome to {store}")

store_new = 'Nick\'s Pizza shop, the "best in town!"'
print(f"Welcome to {store_new}")

day = 24
month = 'October'
temp = -30
#f strings allow you to embed variables directly in the string using curly braces {}
print(f"Today is {day} {month} and the temperature is {temp}°C")

# Make a ariable called day_name and set it to day of the week like Tuesdy and addit to the string we print
day_name = 'Tuesday'
print(f"Today is {day_name}, {day} {month} and the temperature is {temp}°C")

light_is_on = False  
if light_is_on:
    print("The light is on")
print("Hello")

if light_is_on:
    print("The light is on")
    print("Hello")

if light_is_on:
    print("The light is on")
else:
    print("The light is off")

weight = 170.5
if weight > 100:
    print("You are overweight")
else:
    print("You are not overweight") 
# Make a variable age, and if someone is over 18 print "You are an adult" else print "You are a minor"
age = 10
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Create a function to find out if a number is even or odd
def is_even_or_odd(number):
    if number % 2 == 0:
        print(f"Number {number} is even")
    else:
        print(f"Number {number} is odd")

is_even_or_odd(5)
is_even_or_odd(10)

import random
random_number = random.randint(1, 10)
print(f"Random number is: {random_number}")
print(f"Random number is: {random.random()}")

lucky_number = random.randint(1, 100)
fortune_number = random.randint(1, 3)
fortune_text = ""
if fortune_number == 1:
    fortune_text = "You will have a great day!"
elif fortune_number == 2:
    fortune_text = "You will find something valuable!"
else:
    fortune_text = "You will meet someone new!"
print(f"Your fortune is: {fortune_text}")

print(f"Your lucky number is: {lucky_number}")

fav_movies = ["Inception", "The Matrix", "Interstellar"]
print(f"My favorite movies are: {fav_movies}")
print(f"My favorite movie is: {fav_movies[0]}")
print(f"Length of the list is: {len(fav_movies)}")
fav_movies.append("The Dark Knight")
print(f"Length of the list is: {len(fav_movies)}")
print(f"My favorite movies are: {fav_movies}")
fav_movies.insert(1, "The Godfather")
print(f"My favorite movies are: {fav_movies}")
del(fav_movies[2])
print(f"My favorite movies are: {fav_movies}")
del(fav_movies[0])
del(fav_movies[0])
del(fav_movies[0])
print(f"My favorite movies are: {fav_movies}")

fav_numbers = [7, 13, 21, 42]
print(f"My favorite numbers are: {fav_numbers}")    
print(f"My favorite number is: {fav_numbers[0]}")
print(f"Length of the list is: {len(fav_numbers)}")

for number in range(10):
    print(f"Hello: {number}")
    print("Hi")

fav_movies = ["Inception", "The Matrix", "Interstellar"]
for movie in fav_movies:
    print(f"My favorite movie is: {movie}")
    print("I really enjoy watching it")

for number in range(1,40):
    print(f"Number is: {number * 2}")

cats = {"Whiskers":5, "Tom":3, "Garfield":7}
print(f"My cats are: {cats}")
print("Length of the dictionary is:", len(cats))
del(cats["Tom"])
print(f"My cats are: {cats}")

print(f"My cat Whiskers is {cats['Whiskers']} years old")
for cat in cats:
    print(f"My cat {cat} is {cats[cat]} years old")

# Create a dictionary with intsfor keys and boolean for values
int_bool_dict = {1: True, 2: False, 3: True}
print(f"My int-bool dictionary is: {int_bool_dict}")
for key in int_bool_dict:
    print(f"Key {key} has value {int_bool_dict[key]}")

numbers = [62, 66, 94, 97, 25, 11, 68, 54, 48, 67]

sum = 0
for number in numbers:
    if number % 2 == 0:
        sum = sum + number
print(f"Sum of even numbers is: {sum}")

text = """This is a multi-line string.
It can span multiple lines.
You can use triple quotes to create multi-line strings.
This is a multi-line string.
It can span multiple lines.
You can use triple quotes to create multi-line strings.
This is a multi-line string.
It can span multiple lines.
You can use triple quotes to create multi-line strings.
This is a multi-line string.
It can span multiple lines.
You can use triple quotes to create multi-line strings.
This is a multi-line string.
It can span multiple lines.
You can use triple quotes to create multi-line strings.
"""
print(text)
print("Length of the string is:", len(text))
print("Number of words in the string is:", len(text.split()))

word_count = {} 

for word in text.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(f"Word count is: {word_count}")

def bark():
    print("Woof!")
    print("Woof!")

for x in range(3):
    bark()

def hello(name):
    print(f"Hello, {name}!")

for name in ["Alice", "Bob", "Charlie"]:
    hello(name) 

def add_numbers(a, b):
    return a + b    

add_result = add_numbers(5, 10)
print(f"Result of addition is: {add_result}")

def dog_info(name, age):
    print(f"My dog's name is {name} and he is {age} years old.")    
dog_info("Buddy", 5)

def double(number):
    return number * 2

result = double(5)
print(f"Result of doubling is: {result}")

def to_uppercase(string):
    return string.upper()

# result = to_uppercase("hello")
# print(f"Result of converting to uppercase is: {result}")

# user_input = input("Enter your name: ")
# print(f"Hello, {user_input}!")  
# print(user_input.upper())

# user_number = input("Enter a number: ")
# print(f"Double of {user_number} is: {int(user_number) * 2}")

# Enter 1 to uppercase a string, 2 to lowercase a string
# upper_or_lower = input("Enter 1 to uppercase a string, 2 to lowercase a string: ")
# if upper_or_lower == "1":
#     user_string = input("Enter a string: ")
#     print(f"Uppercase string is: {user_string.upper()}")
# elif upper_or_lower == "2":
#     user_string = input("Enter a string: ")
#     print(f"Lowercase string is: {user_string.lower()}") 

def has_remainder(number1, number2):
    if number1 % number2 == 0:
        return False
    else:
        return True 

import time
print("Welcome to the number guessing game!")
time.sleep(1)
guess = int(input("Guess a number between 1 and 10: "))
correct_number = random.randint(1, 10)
while guess != correct_number:
    if guess < correct_number:
        guess = int(input("You need to guess higher! Guess a number between 1 and 10: "))
    else:
        guess = int(input("You need to guess lower! Guess a number between 1 and 10: "))
    time.sleep(1)
print(f"Congratulations! You guessed the correct number: {correct_number}")