import requests

# https://sv443.net/jokeapi/v2/

categories = ["Programming", "Misc", "Pun", "Spooky", "Christmas", "Dark"]

# Hvilke kategorier vi ikke vil ha
params = ["blacklistFlags=racist,sexist"]

category_choice = input("Choose between: Programming, Misc, Pun, Spooky, Christmas, Dark")


def get_category(category_list, user_choice):
    for category in category_list:
        if category == user_choice:
            return category


baseURL = f"https://v2.jokeapi.dev/joke/{get_category(categories, category_choice)}?"


def get_joke():
    response = requests.get(baseURL,
                            headers={"Accept": "application/json"},
                            params={"term": params})

    data = response.json()

    print(data["setup"] + " " + data["delivery"])


get_joke()
