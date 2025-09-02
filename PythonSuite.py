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
        print("="*5,"Console Calculator","="*5)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Floor Division")
        print("8. Absolute Value")
        print("9. Square Root")
        print("10. Exit")
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
            print("="*5,"Console Calculator","="*5)
            break
        else:
            print("No Operation Going to Main Menu")
        
        # Map user choice to the corresponding calculator operation
        match ch:
            case 1:print("Result : " , c.additon(a,b))
            case 2:print("Result : " , c.subtraction(a,b))
            case 3:print("Result : " , c.multiplication(a,b))
            case 4:print("Result : " , c.division(a,b))
            case 5:print("Result : " , c.modulus(a,b))
            case 6:print("Result : " , c.exponentiation(a,b))
            case 7:print("Result : " , c.floor_division(a,b))
            case 8:print("Result : " , c.Absolute_Value(a))
            case 9:print("Result : " , c.sqaure_root(a))

# Function to handle various unit conversions
def unitconversion():
    while True:
        print("="*5,"Unit Conversion","="*5)
        print("Unit Converter")
        print("1. Length")
        print("2. Area")
        print("3. Volume")
        print("4. Mass")
        print("5. Temperature")
        print("6. Speed")
        print("7. Pressure")
        print("8. Energy")
        print("9. Power")
        print("10. Storage")
        print("11. Exit")
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
                print(tabulate(table, headers=["Type", "Unit", "Value"], tablefmt="grid"))
            case 2:
                print("Area Conversion", a, "To", b, un.area_convert(value, a, b))
            case 3:
                print("Volume Conversion", a, "To", b, un.volume_convert(value, a, b))
            case 4:
                print("Mass Conversion", a, "To", b, un.mass_convert(value, a, b))
            case 5:
                print("Temperature Conversion", a, "To", b, un.temp_convert(value, a, b))
            case 6:
                print("Speed Conversion", a, "To", b, un.speed_convert(value, a, b))
            case 7:
                print("Pressure Conversion", a, "To", b, un.pressure_convert(value, a, b))
            case 8:
                print("Energy Conversion", a, "To", b, un.energy_convert(value, a, b))
            case 9:
                print("Power Conversion", a, "To", b, un.power_convert(value, a, b))
            case 10:
                print("Storage Conversion", a, "To", b, un.storage_convert(value, a, b))



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