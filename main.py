import operator as o
import random as r


def guard_one():
    answer_test1 = int(input(f"Hva er svaret på {num1} {operator} {num2} {operator} {num3}?"))
    # Vakt 1
    if answer_test1 == int(eval(f"{num1} {operator} {num2} {operator} {num3}")):
        print("Du bestod testen og kan gå videre til neste test!")
        guard_two()
    else:
        print("Feil svar, hade bra :)")
        exit()


def guard_two():
    # Vakt 2
    test1 = num1 > num2
    test2 = num1 <= num3
    print("Du skal nå bli testet i logiske uttrykk!")
    answer_test2 = input(f"Er det sant at {num1} > {num2}")
    if answer_test2 == "True" or "true":
        print("Du bestod testen og kan gå videre til neste test!")
    else:
        print("Feil svar, hade bra :)")
        exit()


def guard_three():
    word = input("Gi meg hvilket som helst ord og så skal jeg si det baklengs!").lower()
    backwards = word[len(word)::-1]
    print(backwards)
    over = True
    return True


print("Prinsen er kidnappet av sjømonsteret Dagon!\n"
      "Dronningen har beordret alle egnede eventyrere til å møte opp på slottet.\n"
      "10000 gullmynter vil bli gitt til den som klarer å redde prinsen.")

print("Men for at vi skal vite at dere er sterke nok til å redde prinsen, vil vaktene på slottet gi"
      "lederen av eventyrerne tester som må bestås før dere kan dra ut. En feil og dere vil bli kastet ut.")

operators = {
    "+": o.add,
    "-": o.sub,
    "/": o.truediv,
    "*": o.mul
}

keys = list(operators)

operator = r.choice(keys)
num1 = r.randint(1, 20)
num2 = r.randint(1, 20)
num3 = r.randint(1, 20)

over = False

while not over:
    guard_one()
    if guard_three():
        print("Du kan nå dra videre til trollmannen!")
        exit()
