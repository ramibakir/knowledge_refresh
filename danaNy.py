import random as r


# Oppgave 3

class Player:
    def __init__(self, name, health, mana, equipment):
        self.name = name
        self.health = health
        self.mana = mana
        self.equipment = equipment


class Seamonster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


# Printer ut spillerliste fra en dict.
def print_player_info(players):
    print("Her er spillerne som skal sloss med deg mot sjømonsteret\n")
    for player_id in players.values():
        print(f"Spiller: {player_id.name}\nLivspoeng: {player_id.health}\nMana: {player_id.mana}\nUtstyr: {player_id.equipment}\n")


def is_dead(player_health):
    if player_health <= 0:
        return True


def get_random_player():
    player = r.choice(list(player_list.values()))
    return player


aragon = Player("Aragon", 150, 50, "Samuraisverd")
frodo = Player("Frodo", 100, 70, "Tryllestav")
legolas = Player("Legolas", 120, 100, "Pil og bue")

seamonster = Seamonster("Dana", 350, r.randint(15, 20))

player_list = {
    "Aragon": aragon,
    "Frodo": frodo,
    "Legolas": legolas
}

print_player_info(player_list)

game_round = int()

starter = r.randint(1, 2)

while True:
    game_round += 1
    print("\n* ROUND " + str(game_round) + " * ")
    starting_player = get_random_player()
    if starter == 1:
        print("\nSjømonsteret angriper først og gjør", seamonster.damage, "skade på", starting_player.name)
        print(f"Etter {seamonster.damage} damage fra {seamonster.name} har {starting_player.name} nå {(starting_player.health - seamonster.damage)} livspoeng igjen")

    user_choice = input("Velg om du vil bruke vanlig angrep eller en magisk formel ")
    print(f"Du har valgt {user_choice}")
    print(f"Rundens spiller er: {starting_player.name}")
    if user_choice == "vanlig angrep":
        damage_done = r.randint(15, 30)
        mana_used = r.randint(5, 10)
        print(f"{starting_player.name} gjør {damage_done} på {seamonster.name}")
        seamonster.health -= damage_done
        print(f"{seamonster.name} har nå {seamonster.health} livspoeng igjen")

        print(f"{starting_player.name} har nå brukt {mana_used} av sin mana og har igjen {(starting_player.mana - mana_used)} mana")

        if is_dead(seamonster.health):
            print(f"{seamonster.name} er knuuuuuuuust")
            exit()
    elif user_choice == "magisk formel":
        damage_done = r.randint(40, 50)
        mana_used = r.randint(15, 25)

        print(f"{starting_player.name} gjør {damage_done} damage på {seamonster.name}")
        seamonster.health -= damage_done
        print(f"{seamonster.name} har nå {seamonster.health} livspoeng igjen")
        print(f"{starting_player.name} har nå brukt {mana_used} av sin mana og har igjen {(starting_player.mana - mana_used)} mana")

        if is_dead(seamonster.health):
            print(f"{seamonster.name} er knuuuuuuuust")
            exit()
    else:
        print("Ukjent kommando")


