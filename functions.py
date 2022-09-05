"""
functions.py

Functions allow us to write our own custom blocks of code that can be re-used
as many times as we want.

The keyword def introduces a function definition. It must be followed by the
function name and the parenthesized list of formal parameters. The statements
that form the body of the function start at the next line and must be indented.

Read more: 
https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions
"""
import random

# function definition stats with def keyword
def my_first_function():
    print("In my first function!")

# function call (to actually execute the function) has no def keyword
my_first_function()

# functions can take parameters, or simply inputs that allow you send
# the function custom values
def say_name(name):
    print(name)

say_name("Jon")
say_name("Sally")

# functions can return values by using the return keyword
def roll_die(num_sides):
    return random.randrange(1, num_sides + 1)
roll = roll_die(2)
print(roll)
roll = roll_die(2)
print(roll)

# functions can be used in other functions
def guess_roll(num_sides, guess):
    roll = roll_die(num_sides)
    print(f"you guess: {guess} roll was: {roll}")
    if guess == roll:
        print('You guessed it!')
    elif guess > roll:
        print("You guessed higher!")
    else:
        print("You guessed lower!")
guess_roll(4, 2)