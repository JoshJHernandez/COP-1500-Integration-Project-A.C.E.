# Code written in Python 3.10
__author__ = "Joshua Hernandez"

# This program is supposed to be a very basic computer assistant that can help
# you with a handful of things.

# I used (https://www.w3resource.com/python-exercises/python-basic-exercise
# -3. php) to help me set up the time variable (Lines 5-7 is not my code.)
import time
import random
import os

username = os.getlogin()

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
# This code is supposed to import the time of the device running the program
# and paste the exact time that the line of code is executed. (It does not
# update)

print("░█████╗░░░░░█████╗░░░░███████╗░░░")
time.sleep(.1)
# The time.sleep command tells python to wait for a specified amount of time
# before printing the next message.
print("██╔══██╗░░░██╔══██╗░░░██╔════╝░░░")
time.sleep(.1)
print("███████║░░░██║░░╚═╝░░░█████╗░░░░░")
time.sleep(.1)
print("██╔══██║░░░██║░░██╗░░░██╔══╝░░░░░")
time.sleep(.1)
print("██║░░██║██╗╚█████╔╝██╗███████╗██╗")
time.sleep(.1)
print("╚═╝░░╚═╝╚═╝░╚════╝░╚═╝╚══════╝╚═╝v2.0")
time.sleep(.1)
print("Acetex Ltd.")
input("Press Enter to continue...")
print("\nHello", username, "My name is Automated Computational Electronic, "
                           "or A.C.E. for "
                           "short!"
      )
time.sleep(1)
print("\nI can only currently help with a couple of things, as I am in "
      "version "
      "2.0")
time.sleep(1)
print("\nRight now you can ask me what the time is, what the basic python"
      " numeric operators are, to use a calculator, to generate a random "
      "number, or to make a number pyramid")
time.sleep(1)
print("How may I help you today?")


def main():
    """
This is the main line of code for the program. What contains all of the options
used to run this code.
    """
    test = input("A) The time. B) (B.P.N.O). C) Calculator. D) Random Number. "
                 "E) Number Pyramid.\n>>> ").upper()
    if test == "A":
        print("Current Time:", current_time)
    # Elif means that it will tell python that if the previous condition is
    # not met go to this one.
    elif test == "B":
        print("[The basic python numeric operators are, [**], [*], [/], [%],"
              "[//], [+], and [-]")
        print("[**] Is used to add a power to a number. So 5**3 would be 5 to "
              "the power of 3.")
        print("[*] Is used for multiplication, so 5*3 would be 5 times 3.")
        print(
            "[/] Is used for division, however this would also print the "
            "remainder, so 5/3 would be 5 divided by 3 "
            "with a "
            "remainder.")
        print(
            "[%] Is used to print the remainder of two numbers when they are"
            "divided. So 5%3 would show what the "
            "remainder of 5/3 is.")
        print(
            "[//] Is used to divide two numbers without printing the "
            "remainder. So 5//3 would be 5 divided by 3 "
            "without "
            "the remainder being printed.")
        print("[+] Is used to add two numbers together. So 5+3 would be 5"
              "plus 3.")
        print("[-] Is used to subtract two numbers. So 5-3 would be "
              "5 minus 3.")
        print("Two of these B.P.N.O can be used for other things, like the"
              "manipulation of string operators.")
        print("[*] and [+] are used for two separate functions.")
        print(
            "[*] Can be used to repeat the given string for however long the "
            "user specifies. So print(Five*5) would "
            "print "
            "the world Five 5 times.")
        print("[+] Is used to concatenate two strings together. So print"
              "(Five+Three) would print FiveThree")
        print("-======================================"
              "=============================================================="
              "=====================================-")
        print("There are also shorthand operators, or shortcut operators."
              "These operators are, [+=], [-=], [%=], "
              "[*=] and [/=].")
        print(
            "These shorthand operators are used as shortcuts, to perform "
            "arithmetic operations utilizing less lines of "
            "code. ")
        print(
            "For example, if you wanted to add two numbers using the shorthand"
            "operator +=, you would write it as "
            "such. "
            "[5 += 5] and it would output 10")
    elif test == "C":
        # ## I used the foundation of a calculator from POGIL 12 and
        # expanded upon it to include all the numeric operators below.
        def add_numbers(num1, num2):
            """
This function is used to add the two numbers inputted by the user.
            :param num1:
            :param num2:
            """
            print(num1, "+", num2, "=", num1 + num2)

        def subtract_numbers(num1, num2):
            """
This function is used to subtract the two numbers inputted by the user.
            :param num1:
            :param num2:
            """
            print(num1, "-", num2, "=", num1 - num2)

        def multiply_numbers(num1, num2):
            """
This function is used to multiply the two numbers inputted by the user.
            :param num1:
            :param num2:
            """
            print(num1, "*", num2, "=", num1 * num2)

        def power_numbers(num1, num2):
            """
This function is used to add exponents to a number. The first number would
be the base, and the second would be the exponent.
            :param num1:
            :param num2:
            """
            print(num1, "**", num2, "=", num1 ** num2)

        def divide_numbers(num1, num2):
            """
This function is used to divide the two numbers inputted by the user.
            :param num1:
            :param num2:
            """
            print(num1, "/", num2, "=", num1 / num2)

        def floor_divide_numbers(num1, num2):
            """
This function is used to divide the two numbers inputted by the user and only
print the number on the left on the decimal.
            :param num1:
            :param num2:
            """
            print(num1, "//", num2, "=", num1 // num2)

        def remainder_division_numbers(num1, num2):
            """
This function is used to divide the two numbers inputted by the user and only
print the remainder.
            :param num1:
            :param num2:
            """
            print(num1, "%", num2, "=", num1 % num2)

        def calculator():
            """
This function is the calculator module of my program. All of the contents below
are the essential parts to run the calculator.
            """
            first_number = int(input("Enter two numbers and then enter "
                                     "an operator to use the "
                                     "calculator.\nEnter the "
                                     "first "
                                     "number:\n>>> "))
            second_number = int(input("Enter the second number:\n>>> "))
            operator = input(
                "Enter a '+' to add a '-' to subtract, a '*' to multiply, a"
                "'**' to use an exponent, a '/' to divide, "
                ":\n>>> ")

            if operator == '+':
                add_numbers(first_number, second_number)
            elif operator == '-':
                subtract_numbers(first_number, second_number)
            elif operator == '*':
                multiply_numbers(first_number, second_number)
            elif operator == '**':
                power_numbers(first_number, second_number)
            elif operator == '/':
                divide_numbers(first_number, second_number)
            elif operator == '//':
                floor_divide_numbers(first_number, second_number)
            elif operator == '%':
                remainder_division_numbers(first_number, second_number)
            else:
                print("Invalid operator!")

        calculator()

    elif test == "D":
        print('Your random number is:', random.randint(1, 10))

    elif test == "E":
        print("Just enter a number below and a triangle will be made using"
              "numbers counting up to the inputted number.")
        # I used code from POGIL 10, where we used nested loops to make
        # shapes like pyramids, and blocks using height, rows and columns.
        height = int(input("Enter height: "))
        for row in range(1, height + 1):
            for column in range(row):
                print(row, end=" ")
            print()
    else:
        print("[ERROR] Invalid option.")


while True:
    main()
    if input('If you would like to return to the main menu type Y, if not '
             'type N (Y/N)\n>>>'
             ).upper() != 'Y':
        break
