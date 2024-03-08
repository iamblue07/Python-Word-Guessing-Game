
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

#Functions


def validate_letter(letter, game_GUI):
    if letter.unicode.isalpha() and letter.isdigit == False:
        game_GUI.get_input_data()[0].set_value(letter.unicode)


def game_start(difficulty_level):
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
    letter = game_GUI.add.text_input("", maxchar=1, onkeypress=lambda x: validate_letter(x, game_GUI))
    app_no = GF.search_letter_in_word(letter, word)
    if app_no == 0:
        health -= 1
    else:
        GF.replace_letter_in_word(app_no,word,hidden_word,letter)
    if health <= 0:
        text_GUI = game_GUI.add.label("You Lost\n")
        letter.hide()
        diff_GUI = game_GUI.add.button("Return to Difficulty Menu", difficulty_level)
        main_GUI = game_GUI.add.button("Return to Main Menu", main_menu)
    game_GUI.mainloop(screen)


def player_name_menu():
    player_menu = pygame_menu.Menu('Player Name', width, height, theme=pygame_menu.themes.THEME_DARK)
    player_menu.add.text_input('Set Player Name:', maxchar=4, onreturn=difficulty_menu)

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
