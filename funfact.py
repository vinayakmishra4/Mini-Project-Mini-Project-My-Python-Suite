import random
import requests

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

def lucky_number(low, high):


def random_fun():
    print("\nRandom Fun Menu:")
    print("1. Lucky Number")
    print("2. Random Fun Fact")
    choice = input("Choose an option: ")

    if choice == "1":
    elif choice == "2":
        print("Fun Fact:", get_random_fact())
    else:
        print("Invalid choice.")