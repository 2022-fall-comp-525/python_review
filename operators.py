"""
operators.py

Python Operators and Operator Precedence

The higher up on the list, the higher the precedence.

**	                        Exponentiation (raise to the power)
~ + -	                    Complement, unary plus and minus
* / % //	                Multiply, divide, modulo and floor division
+ -	                        Addition and subtraction
>> <<	                    Right and left bitwise shift
&	                        Bitwise 'AND'td>
^ |	                        Bitwise exclusive `OR' and regular `OR'
<= < > >=	                Comparison operators
<> == !=	                Equality operators
= %= /= //= -= += *= **=	Assignment operators
is is not	                Identity operators
in not in	                Membership operators
not or and	                Logical operators
"""

print(2 + 2) # Addition
print(2-1) # Subtraction
print(3*3)  # Multiplication
print(2**4) # Exponentiation
print(3/2) # Division
print(3%2) # Modulo (get the remainder of division)
print(7//2) # Floor division

# Precedence example, the * operator has higher precedence and gets executed
# before the addition operator
print(2+1*10)

# Note, the assignment operator = has one of the lowest precendents as thus
# normally gets executed last. This means you can have complicated expressions
# assigned to variables
some_variable = 10 * 3 // 2 ** 2
print(some_variable)
