import random


def extract_from_file(_file_name):
    with open(_file_name, "r") as _file:
        return random.choice(_file.readlines()).strip().lower()


def search_letter_in_word(letter, word):
    app_no = 0
    for iterator in word:
        if iterator == letter:
            app_no += 1
    return app_no



def replace_letter_in_word(app_no, word, empty_word, letter):
    aux = list(empty_word)
    i = 0
    while app_no != 0 and i < len(word):
        if word[i] == letter:
            aux[i] = letter
            app_no -= 1
        i += 1
    empty_word = ''.join(aux)
    return empty_word


def read_a_letter():
    char = input("Introduce a single character:")
    if not char.isdigit():
        if len(char) == 1:
            return char
        else:
            print("You introduced more than a character!")
    else:
        print("You entered a number!")


def remaining_tries(life, word, empty_word):
    if life != 0:
        print(f"Tries left: {life} \n")
    else:
        print("You lost!")
        print(f"The word was: {word}")
        print(f"Letters guessed correctly: {empty_word} \n")


def create_empty_word(word):
    empty_word = "-" * len(word)
    return empty_word


def menu():
    print("MENU")
    print("1 - Begin the game")
    print("2 - Add new words in the game")
    print("3 or more - Close the game")
    _option = input()
    if _option.isdigit() == True:
        return int(_option)
    else:
        print("You didn't introduce a digit!")
        return menu()


def difficulty_menu():
    print("Choose difficulty level:")
    print("1-Easy")
    print("2-Medium")
    print("3-Hard")
    print("4-Very hard")
    print("5 or more - Go back")
    _option = input()
    if _option.isdigit() == True:
        return int(_option)
    else:
        print("You didn't introduce a digit!")
        return difficulty_menu()

def check_game_won(_empty_word):
    for iterator in _empty_word:
        if iterator == "-":
            return 0
    return 1


def game(_file_name):
    life = 5
    word = extract_from_file(_file_name)
    empty_word = create_empty_word(word)
    print(f"Tries left: {life}")
    pas = 0
    while pas == 0:
        letter = read_a_letter()
        app_no = search_letter_in_word(letter, word)
        if app_no == 0:
            life -= 1
            remaining_tries(life, word, empty_word)
            if life == 0:
                pas = 1

        else:
            empty_word = replace_letter_in_word(app_no, word, empty_word, letter)
            if check_game_won(empty_word):
                print("You Won!")
                print(f"The word was {empty_word} \n")
                pas = 1
        if pas == 0:
            print(empty_word)
