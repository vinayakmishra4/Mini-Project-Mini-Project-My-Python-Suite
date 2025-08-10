# Mini Project Python Suite
import Calc as c
def Calaculator():
    
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
    ch=int(input("Enter your choice: "))

    if ch >=1 and ch <= 6:
        print("-"*10)
        a=int(input("Enter the First Number: "))
        b=int(input("Enter the Second Number: "))
        print("-"*10)
    
    if ch == 8 or ch == 9:
        print("-"*10)
        a=int(input("Enter the First Number: "))
        print("-"*10)
    