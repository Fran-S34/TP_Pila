import sys

sys.path.append(r"C:\Users\franc\Desktop\UADER\algoritmos_2026_todo")

from stack import Stack


def find_position(character_stack: Stack, character_name: str) -> int:
    character_aux = Stack()
    position = 1
    result = None

    while character_stack.size() > 0:
        character = character_stack.pop()
        character_aux.push(character)

        if character["name"] == character_name:
            result = position

        position += 1

    while character_aux.size() > 0:
        character_stack.push(character_aux.pop())

    return result


def characters_with_more_than(character_stack: Stack, amount: int) -> None:
    character_aux = Stack()

    while character_stack.size() > 0:
        character = character_stack.pop()
        character_aux.push(character)

        if character["movies"] > amount:
            print(character["name"], character["movies"])

    while character_aux.size() > 0:
        character_stack.push(character_aux.pop())


def count_movies(character_stack: Stack, character_name: str) -> int:
    character_aux = Stack()
    result = None

    while character_stack.size() > 0:
        character = character_stack.pop()
        character_aux.push(character)

        if character["name"] == character_name:
            result = character["movies"]

    while character_aux.size() > 0:
        character_stack.push(character_aux.pop())

    return result


def characters_starting_with(character_stack: Stack, initials: tuple) -> None:
    character_aux = Stack()

    while character_stack.size() > 0:
        character = character_stack.pop()
        character_aux.push(character)

        if character["name"][0].upper() in initials:
            print(character["name"])

    while character_aux.size() > 0:
        character_stack.push(character_aux.pop())


if __name__ == "__main__":
    characters = Stack()

    mcu_characters = [
        {"name": "Iron Man", "movies": 10},
        {"name": "Thor", "movies": 8},
        {"name": "Black Widow", "movies": 9},
        {"name": "Captain America", "movies": 10},
        {"name": "Doctor Strange", "movies": 4},
        {"name": "Rocket Raccoon", "movies": 5},
        {"name": "Groot", "movies": 6},
        {"name": "Hulk", "movies": 8},
    ]

    for character in mcu_characters:
        characters.push(character)

    print("posicion Rocket Raccoon:", find_position(characters, "Rocket Raccoon"))
    print("posicion Groot:", find_position(characters, "Groot"))

    print("\nparticiparon en mas de 5 peliculas:")
    characters_with_more_than(characters, 5)

    print("\npeliculas de Black Widow:", count_movies(characters, "Black Widow"))

    print("\nnombres que empiezan con C, D o G:")
    characters_starting_with(characters, ("C", "D", "G"))