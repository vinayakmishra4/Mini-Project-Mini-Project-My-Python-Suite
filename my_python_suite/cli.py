# python_suite/cli.py

from python_suite import calc, unitconvert, funfact


def main():
    while True:
        print("\n=== Python Suite ===")
        print("1. Calculator")
        print("2. Unit Converter")
        print("3. Fun Facts")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            calc.run()   # calls calculator menu
        elif choice == "2":
            unitconvert.run()  # calls unit converter
        elif choice == "3":
            funfact.run()  # calls fun fact generator
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()