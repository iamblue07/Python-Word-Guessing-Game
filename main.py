import Game_Functions as GF


if __name__ == '__main__':
    game_on = 1
    while game_on == 1:
        option = GF.menu()
        if option == 1:
            difficulty_level = GF.difficulty_menu()
            if difficulty_level == 1:
                file_name = "Easy"
                GF.game(file_name)
            if difficulty_level == 2:
                file_name = "Medium"
                GF.game(file_name)
            if difficulty_level == 3:
                file_name = "Hard"
                GF.game(file_name)
            if difficulty_level == 4:
                file_name = "Very Hard"
                GF.game(file_name)
        if option == 2:
            new_word = input("Introduce a new word:")
            if not new_word.isalpha():
                print("Error: the word contains spaces, numbers, symbols or non-standard letters!")
            elif len(new_word) < 3:
                print("Error: word too short")
            else:
                file_save = "Word_Error_Save"
                if 3 <= len(new_word) <= 5:
                    file_save = "Easy"
                elif 6 <= len(new_word) <= 9:
                    file_save = "Medium"
                elif 10 <= len(new_word) <= 14:
                    file_save = "Hard"
                elif len(new_word) > 14:
                    file_save = "Very Hard"
                with open(file_save, "a") as file:
                    file.write("\n")
                    file.write(new_word.lower())
        if option >= 3:
            game_on = 0
            print("Thank you for playing!")
