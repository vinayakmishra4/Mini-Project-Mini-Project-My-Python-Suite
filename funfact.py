import random
import requests
import datetime
import hashlib


def get_random_fact():
    """Fetch a random fact from the internet."""
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    try:
        response = requests.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()
        data = response.json()
        return data.get("text")
    except requests.exceptions.RequestException as e:
        return f"Error fetching fact: {e}"

def lucky_number():
    """Generate a random lucky number between low and high."""

def random_fun():
    print("\nRandom Fun Menu:")
    print("1. Lucky Number")
    print("2. Random Fun Fact")
    choice = input("Choose an option: ")
    if choice == "1":
        low = int(input("Enter the lower bound: "))
        high = int(input("Enter the upper bound: "))
        print("Your lucky number is:", lucky_number(low, high))
    elif choice == "2":
        print("Fun Fact:", get_random_fact())
    else:
        print("Invalid choice.")