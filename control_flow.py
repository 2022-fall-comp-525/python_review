"""
control_flow.py

The default flow (or control flow) of a Python module is to start at the 
first line and continue line by line until the end of the file.

We have several ways to alter this and control the flow of execution.

read more: https://docs.python.org/3/tutorial/controlflow.html
"""

# Most basic, if/else conditionals. Use the "if" statement to do something,
# or not do something, based on the value of some condition.
if True:
    print("this will always print, because the conditional is True!")
if False:
    print("this will never print, because the conditional is False!")

if 1 == 1:
    print("this will always print, because the conditional evaluates to True!")
if 1 == 2:
    print("this will never print, because the conditional evaluates to False!")

coin_flip = "heads"
if coin_flip == "heads":
    print("flipped heads!")
else:
    print("flipped tails!")

four_sided_die_roll = 2
if four_sided_die_roll == 1:
    print("rolled 1")
elif four_sided_die_roll == 2:
    print("rolled 2")
elif four_sided_die_roll == 3:
    print("rolled 3")
elif four_sided_die_roll == 4:
    print("rolled 4")
else:
    print("unkown roll!")

# for statements allow you execute the same code for a given number of times
# normal usage is:
# for some_variable in [iterable]
for name in ['jon', 'sally', 'sue']:
    print(name)
for character in 'hello world!':
    print(character)

# can also do:
# for some_variable in range(stop)
for i in range(3):
    print(f"i is {i}")
# or for some_variable in range(start, stop)
for i in range(5, 10):
    print(f"i is {i}")
# or for some_variable in range(start, stop, step)
for i in range(1, 10, 2):
    print(f"i is {i}")

# the "while" statement also can be used to execute code until a condition
# evaluates to False
counter = 0
while counter < 5:
    print(f"counter is {counter}")
    counter += 1
