# Notes for MidTerm

THE SOFTWARE DEVELOPMENT PROCESS
# 1. Analyze the Problem
#      Do we understand the exact problem to be solved?
# 2. Determine the Specifications:
#      What are the inputs, outputs, and how they relate to one another?
#      Here we list each input, each output, and how they relate to each other
# 3. Create a Design
#      This is the pseudocode of your program
#      Here we write an algorithm line by line in general English
# 4. Implement the Design
#      Write it in Python
#      Here we convert the pseudocode to actual code
# 5. Test/Debug the Program
# 6. Maintain the Program
#       If you follow these steps, coding should be easier
#       If you skip them, it will become more challenging

# 1. Analysis – the temperature is given in Celsius, but the user wants it expressed in degrees Fahrenheit.
# 2. Specification-
#     Input – temperature in Celsius
#     Output – temperature in Fahrenheit
#     Output = 9/5 * (input) + 32
# 3. Pseudocode:
#     Input the temperature in degrees Celsius (call it celsius)
#     Calculate fahrenheit as (9/5)*celsius+32
#     Output fahrenheit
# 4. Now we need to implement the design in Python!
# 5. And don’t forget to test and debug


FUNCTIONS
#PASSING PARAMETERS
#convert.py
def main():
    Fahrenheit = eval(input("What is the Fahrenheit temperature?"))
    Celsius = (Fahrenheit-32) * 5 / 9

    print("The temperature is", Celsius ,"degrees Celsius")

main()

#OR
# RETURNING VALUES

def main():
celsius = eval(input("What is the Celsius temperature? ")) print("The temperature is", temperature(celsius), "degrees
       Fahrenheit.")
 def temperature(C):
     F = (9/5) * C + 32
     return F
main()

# Notice how the variable celsius is passed to temperature()
#        C in temperature() then equals celsius
#        F is returned exactly where temperature(celsius) has been called.
#        Remember! Functions should be defined before they are run!
#        main() cannot be placed before def main()

SENTINEL LOOP WITH PRIMING READ
# average4.py
# A program to average a set of numbers
# Illustrates sentinel loop using empty string as sentinel
def main(): sum = 0.0 count = 0
xStr = input("Enter a number (<Enter> to quit) >> ") while xStr != "":
x = float(xStr)
sum = sum + x
count = count + 1
xStr = input("Enter a number (<Enter> to quit) >> ")
print("\nThe average of the numbers is", sum / count) main()

#This is an interactive loop because the user is providing input at each loop
# It utilizes a sentinel “”. As long as the input entered is NOT “”, the loop continues
#  xStr = input("Enter a number (<Enter> to quit) >> ")is the priming read

SEEDING THE LOOP AND INPUT VALIDATION
# Another option is seeding the loop.
# In this case an invalid value is given to begin the loop
#        Rather than an input() prior to the loop with the priming read
# An example of this is the following
#        number = -1# start with an illegal value while number <= 0: # to get into the loop
#          number = float(input("Enter a positive number: "))
#          The loop will not start until a positive number is provided
# We can use this for input validation
#          The loop does not start until a proper input is provided
#          We could use this to ensure numbers are entered, words etc.

FOR LOOPS WITH RANGE ():
# average1.py
# A program to average a set of numbers
# Illustrates counted loop with accumulator
def main():
n = int(input("How many numbers do you have? ")) sum = 0.0
for i in range(n):
x = float(input("Enter a number >> "))
sum = sum + x
print("\nThe average of the numbers is", sum / n)
main()
#This is a definite/counted loop because it will run through the precise number of items in the list.
# In this case range(n) tells it to cycle n times from 0 to n-1

FOR LOOPS WITH A LIST []:
# average1_altered.py
# A program to average a set of numbers
# Illustrates counted loop with accumulator
def main():
    sum = 0.0
    count = 0
for i in [1, 2, 3, 4, 5]: sum = sum + i
count = count + 1
print("\nThe average of the numbers is", sum / count)

# This is a definite/counted loop because it will run through the precise number of items in the list.
# In this case 5 items.
# Note: It can cycle through numbers, strings of text, etc.
# Whatever is in the list between commas is considered 1 item

ACCUMULATOR
# In both examples an accumulator was used
#       It was sum and count
#       We build up or “accumulate” a final valuE
#       piece by piece.
#       It is NOT just used for addition
#       We CAN have multiple accumulators in a single program

IF-ELIF-ELSE STATEMENT
# quadratic4.py
import math
def main():
print("This program finds the real solutions to a quadratic\n")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
discrim = b * b - 4 * a * c if discrim < 0:
print("\nThe equation has no real roots!") elif discrim == 0:
        root = -b / (2 * a)
print("\nThere is a double root at", root) else:
discRoot = math.sqrt(b * b - 4 * a * c) root1 = (-b + discRoot) / (2 * a)
root2 = (-b - discRoot) / (2 * a) print("\nThe solutions are:", root1, root2 )
  main()

#This version checks for errors when doing math:

# quadratic5.py
# A program that demonstrates exception handling
import math
def main():
print ("This program finds the real solutions to a quadratic\n")
try:
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: ")) discRoot = math.sqrt(b * b - 4 * a * c) root1 = (-b + discRoot) / (2 * a)
root2 = (-b - discRoot) / (2 * a) print("\nThe solutions are:", root1, root2)
    except ValueError:
        print("\nNo real roots")
  main()



IF-ELIF-ELSE AND EXCEPTION HANDLING
#A simple decision will have an
#          if
# A two-way decision
#         if-else
# A multi-way decision
#          if-elif-else, wherein all conditions that are not first or last are elif
# Exception handling always uses try-except
#      The body is under the try condition
#      The exceptions are under the except conditions
#      You can have multiple exceptions, one for each error
#      Writing a general except with nothing else, will cover all exceptions not previously listed
# In both sets of statements, the program will only move to the next statement, if the first is NOT True.
#         It will never arrive at ELSE if the condition with IF is true


THE LIST DATA TYPE
# >>> myList = [1, "Spam ", 4, "U"]
# >>> myList[0]
# 1
# >>> myList[0:2] [1, 'Spam '] >>> myList[-1] 'U'
# >>> myList[2:] [4, 'U']

# Remember that we can refer to parts of a list too
#    Each item is the next number in the string.
#    An item can be a character, a number, a long string, etc.
#    Note this is different than a string


STRING FORMATTING
# >>> "Hello {0} {1}, you may have won ${2}." .format("Mr.", "Smith", 10000)
#                'Hello Mr. Smith, you may have won $10000.'
# >>> 'This int, {0:5}, was placed in a field of width 5'.format(7)
#                'This int,     7, was placed in a field of width 5'
# >>> 'This int, {0:10}, was placed in a field of width 10'.format(10)
#                 'This int,         10, was placed in a field of width 10'
# >>> 'This float, {0:10.5}, has width 10 and precision 5.'.format(3.1415926)
#                'This float,    3.1416, has width 10 and precision 5.'
# >>> 'This float, {0:10.5f}, is fixed at 5 decimal places.'.format(3.1415926)
#                'This float,    3.14159, is fixed at 5 decimal places.'
# >>> "Compare {0}, {0:0.10}, and {0:0.10f}".format(3.14)
#                 'Compare 3.14, 3.14, and 3.1400000000'

#Note: without the f,
# the precision is based on the number of digits listed, with the f, the precise decimal is determined
# If you are interested in more thorough types of formatting, you can explore on your own.


STRING: HELLO BOB (8 DIGITS INCLUDING THE SPACE)
# 012345678
# >>> greet = "Hello Bob"
# >>> greet[0] 'H'
# >>> greet[0:3] 'Hel'
# >>> greet[5:9] ' Bob'
# >>> greet[:5] 'Hello'
# >>> greet[5:] ' Bob'
# >>> greet[-3] 'B'

PYTHON VS MATHEMATICS  ---- MEANING
<            <             Less than
<=           ≤             Less than or equal to
==           =             Equal to
>=           ≥             Greater than or equal to
>            >             Greater than
!=           ≠             Not equal to