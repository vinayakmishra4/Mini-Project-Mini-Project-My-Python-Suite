# Project Python Suite
"""
This script is a Python Suite that offers multiple utilities:
1. A Console Calculator supporting addition, subtraction, multiplication, division, modulus, exponentiation, floor division, absolute value, and square root operations.
2. A Unit Converter that can convert between various units of length, area, volume, mass, temperature, speed, pressure, energy, power, and storage.
3. A Random number and fact generator.

Users can interact with the suite via a menu-driven interface.
"""

from numpy import double
import Calc as c
import UnitConvert as un
import random
import funfact as fun
from colorama import Fore, Style, init
from tabulate import tabulate
import argparse

init(autoreset=True)

# Function to handle the calculator operations menu
def Calaculator():
    while True:
        print(Fore.CYAN + "="*5 + " Console Calculator " + "="*5 + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Addition")
        print(Fore.YELLOW + "2. Subtraction")
        print(Fore.YELLOW + "3. Multiplication")
        print(Fore.YELLOW + "4. Division")
        print(Fore.YELLOW + "5. Modulus")
        print(Fore.YELLOW + "6. Exponentiation")
        print(Fore.YELLOW + "7. Floor Division")
        print(Fore.YELLOW + "8. Absolute Value")
        print(Fore.YELLOW + "9. Square Root")
        print(Fore.RED + "10. Exit" + Style.RESET_ALL)
        ch=int(input("Enter your choice: "))

        # For operations requiring two numbers (addition to exponentiation)
        if ch >=1 and ch <= 6:
            print("-"*10)
            a=double(input("Enter the First Number: "))
            b=double(input("Enter the Second Number: "))
            print("-"*10)
    
        # For operations requiring only one number (absolute value and square root)
        elif ch == 8 or ch == 9:
            print("-"*10)
            a=int(input("Enter the First Number: "))
            print("-"*10)
        elif ch == 10:
            print("Thank You")
            print(Fore.CYAN + "="*5 + " Console Calculator " + "="*5 + Style.RESET_ALL)
            break
        else:
            print("No Operation Going to Main Menu")
        
        # Map user choice to the corresponding calculator operation
        match ch:
            case 1:print(Fore.GREEN + "Result : " + str(c.additon(a,b)) + Style.RESET_ALL)
            case 2:print(Fore.GREEN + "Result : " + str(c.subtraction(a,b)) + Style.RESET_ALL)
            case 3:print(Fore.GREEN + "Result : " + str(c.multiplication(a,b)) + Style.RESET_ALL)
            case 4:print(Fore.GREEN + "Result : " + str(c.division(a,b)) + Style.RESET_ALL)
            case 5:print(Fore.GREEN + "Result : " + str(c.modulus(a,b)) + Style.RESET_ALL)
            case 6:print(Fore.GREEN + "Result : " + str(c.exponentiation(a,b)) + Style.RESET_ALL)
            case 7:print(Fore.GREEN + "Result : " + str(c.floor_division(a,b)) + Style.RESET_ALL)
            case 8:print(Fore.GREEN + "Result : " + str(c.Absolute_Value(a)) + Style.RESET_ALL)
            case 9:print(Fore.GREEN + "Result : " + str(c.sqaure_root(a)) + Style.RESET_ALL)

# Function to handle various unit conversions
def unitconversion():
    while True:
        print(Fore.CYAN + "="*5 + " Unit Conversion " + "="*5 + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Length")
        print(Fore.YELLOW + "2. Area")
        print(Fore.YELLOW + "3. Volume")
        print(Fore.YELLOW + "4. Mass")
        print(Fore.YELLOW + "5. Temperature")
        print(Fore.YELLOW + "6. Speed")
        print(Fore.YELLOW + "7. Pressure")
        print(Fore.YELLOW + "8. Energy")
        print(Fore.YELLOW + "9. Power")
        print(Fore.YELLOW + "10. Storage")
        print(Fore.RED + "11. Exit" + Style.RESET_ALL)
        ch=int(input("Enter your choice: "))
        # Prompt user for value and units to convert from and to
        if ch >=1 and ch <= 10:
            print("-"*10)
            value=double(input("Enter the value: "))
            a=input("Form Repctive Unit : ")
            b=input("To Repctive Unit : ")
        else:
            print("No Operation Going to Main Menu")
            break

        # Map user choice to the corresponding conversion function
        match ch:
            case 1:
                result = un.length_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 2:
                result = un.area_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 3:
                result = un.volume_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 4:
                result = un.mass_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 5:
                result = un.temp_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 6:
                result = un.speed_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 7:
                result = un.pressure_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 8:
                result = un.energy_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 9:
                result = un.power_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)
            case 10:
                result = un.storage_convert(value, a, b)
                table = [["From", a, value], ["To", b, result]]
                print(Fore.GREEN + tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid") + Style.RESET_ALL)



parser = argparse.ArgumentParser(description="Python Suite - A collection of utilities")
parser.add_argument("--help-menu", action="store_true", help="Show available options at startup")
args = parser.parse_args()

if args.help_menu:
    print("""
    Python Suite Options:
    1. Calculator - Perform mathematical operations
    2. Unit Converter - Convert between different units
    3. Random number and fact - Generate random fun facts
    """)
    exit()

# Main menu of the Python Suite that ties all modules together
while True:
    print(Fore.CYAN + "="*5 + " Python Suite " + "="*5 + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Calculator")
    print(Fore.YELLOW + "2. Unit Converter")
    print(Fore.YELLOW + "3. Random number and fact")
    print(Fore.RED + "4. Exit" + Style.RESET_ALL)

    ch=int(input("Enter your choice: "))
    match ch:
        case 1:Calaculator()
        case 2:unitconversion()
        case 3:fun.random_fun()
        case 4:print("Thank you for using Python Suite") ; break
    
    print("="*10)