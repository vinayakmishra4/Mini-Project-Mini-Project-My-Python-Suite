# Project Python Suite

from numpy import double
import Calc as c
import UnitConvert as un
import random
import funfact as fun

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

        if ch >=1 and ch <= 6:
            print("-"*10)
            a=double(input("Enter the First Number: "))
            b=double(input("Enter the Second Number: "))
            print("-"*10)
    
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
        if ch >=1 and ch <= 10:
            print("-"*10)
            value=double(input("Enter the value: "))
            a=input("Form Repctive Unit : ")
            b=input("To Repctive Unit : ")
        else:
            print("No Operation Going to Main Menu")
            break

        match ch:
            case 1:
                print("Length Conversion", a, "To", b, un.length_convert(value, a, b))
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



while True:
    print("="*5,"Python Suite","="*5)
    print("1. Calculator")
    print("2. Unit Converter")
    print("3. Random number and fact")
    print("4. Exit")

    ch=int(input("Enter your choice: "))
    match ch:
        case 1:Calaculator()
        case 2:unitconversion()
        case 3:fun.random_fun()
        case 4:print("Thank you for using Python Suite") ; break
    
    print("="*10)


    