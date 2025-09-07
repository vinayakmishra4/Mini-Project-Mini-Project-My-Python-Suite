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
        a=float(input("Enter first number: ")) if ch != 8 and ch != 9 else a = float(input("Enter number: "))
        b=float(input("Enter second number: ")) if ch <= 7 else 0
        match ch:
            case 1: print(Fore.GREEN + "Result : " + str(c.additon(a,b)) + Style.RESET_ALL)
            case 2: print(Fore.GREEN + "Result : " + str(c.subtraction(a,b)) + Style.RESET_ALL)
            case 3: print(Fore.GREEN + "Result : " + str(c.multiplication(a,b)) + Style.RESET_ALL)
            case 4: print(Fore.GREEN + "Result : " + str(c.division(a,b)) + Style.RESET_ALL)
            case 5: print(Fore.GREEN + "Result : " + str(c.modulus(a,b)) + Style.RESET_ALL)
            case 6: print(Fore.GREEN + "Result : " + str(c.exponentiation(a,b)) + Style.RESET_ALL)
            case 7: print(Fore.GREEN + "Result : " + str(c.floor_division(a,b)) + Style.RESET_ALL)
            case 8: print(Fore.GREEN + "Result : " + str(c.Absolute_Value(a)) + Style.RESET_ALL)
            case 9: print(Fore.GREEN + "Result : " + str(c.sqaure_root(a)) + Style.RESET_ALL)
            case 10: break

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
        if ch >=1 and ch <=10:
            value = float(input("Enter value to convert: "))
            a = input("From unit: ")
            b = input("To unit: ")
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
            case 11:
                break

# Main function for setup.py entry point
def main():
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
        return

    while True:
        print(Fore.CYAN + "="*5 + " Python Suite " + "="*5 + Style.RESET_ALL)
        print(Fore.YELLOW + "1. Calculator")
        print(Fore.YELLOW + "2. Unit Converter")
        print(Fore.YELLOW + "3. Random number and fact")
        print(Fore.RED + "4. Exit" + Style.RESET_ALL)

        ch = int(input("Enter your choice: "))
        match ch:
            case 1: Calaculator()
            case 2: unitconversion()
            case 3: fun.Fun()
            case 4:
                print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
                break

if __name__ == "__main__":
    main()