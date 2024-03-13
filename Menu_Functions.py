
#Imports

import pygame
import pygame_menu
from screeninfo import get_monitors

import Game_Functions as GF

#Variables

primary_monitor = get_monitors()[0]
width = primary_monitor.width
height = primary_monitor.height
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
player_name = "ANON"
letter = ""
word = ""
hidden_word = ""
health = 0
app_no = 0

#Functions


def CheckLetter(input):
    global word
    global hidden_word
    global app_no
    global health
    app_no = GF.search_letter_in_word(input, word)
    if app_no > 0:
        hidden_word=GF.replace_letter_in_word(app_no, word, hidden_word, input)
    else:
        health -= 1


def ChangePlayerName(input):
   global player_name
   player_name = input

def validate_letter(letter, game_GUI):
    if letter.unicode.isalpha() and letter.isdigit == False:
        game_GUI.get_input_data()[0].set_value(letter.unicode)



def game_start(difficulty_level):
    global word
    global hidden_word
    global health
    game_GUI = pygame_menu.Menu(f"Difficulty: {difficulty_level}", width, height, theme=pygame_menu.themes.THEME_DARK)
    file_name = ""
    health = 5
    if difficulty_level == 'Easy':
        file_name = "Easy"
    if difficulty_level == 'Medium':
        file_name = "Medium"
    if difficulty_level == 'Hard':
        file_name = "Hard"
    if difficulty_level == 'Very Hard':
        file_name = "Very Hard"

    word=GF.extract_from_file(file_name)
    hidden_word=GF.create_empty_word(word)
    hidden_word_GUI = game_GUI.add.label(hidden_word)
    health_GUI = game_GUI.add.label(f"Lives Left: {health}")
    text_GUI = game_GUI.add.label("Introduce a letter:\n")
    if health != 0:
        text_input_GUI=game_GUI.add.text_input("", maxchar=1, onreturn=CheckLetter)
    else:
        text_GUI = game_GUI.add.label("You Lost\n")
    game_GUI.mainloop(screen)


def player_name_menu():
    player_menu = pygame_menu.Menu('Player Name', width, height, theme=pygame_menu.themes.THEME_DARK)
    player_menu.add.text_input('Set Player Name:', maxchar=4, onreturn=difficulty_menu, onchange=ChangePlayerName)
    player_menu.mainloop(screen)


def difficulty_menu(player_name):
    difficulty = pygame_menu.Menu('Difficulty', width, height, theme=pygame_menu.themes.THEME_DARK)
    difficulty.add.label('Select Difficulty\n\n', font_size=50)
    difficulty.add.button('Easy', game_start, 'Easy')
    difficulty.add.button('Medium', game_start, 'Medium')
    difficulty.add.button('Hard', game_start, 'Hard')
    difficulty.add.button('Very Hard', game_start, 'Very Hard')
    difficulty.add.label('\n\n')
    difficulty.add.button('Go Back', main_menu)

    difficulty.mainloop(screen)


def main_menu():
    menu = pygame_menu.Menu('Main Menu', width, height,
                            theme=pygame_menu.themes.THEME_DARK)

    menu.add.button('Play', player_name_menu)
    menu.add.button('Leaderboard(To be Implemented)')
    menu.add.button('Settings (To be Implemented)')
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(screen)
