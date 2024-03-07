This is a Python project I'm currently working on as a way to learn on my own how to use different Python libraries.
For now I am using the following libraries: random, pygame and pygame_menu.
So far the game is playable through the console. There are 5 difficulty levels, each based on the number of letters a word has. The words are saved in different .txt files, based on their length. The user can also add new words and they will automatically be added to the corresponding difficulty level based on the word's number of letters. Every time the user guesses a letter correctly, every occurrence of it is shown. The other letters are hidden with a '-' character. The game ends when the user guesses all the letters correctly or when he guesses wrong 5 times.
The game has multiple validations to check for incorrect inputs (using numbers instead of letters and vice versa, typing multiple letters instead of one etc)
I'm currently working on making a graphic interface using pygame and pygame_menu, however this is in early development stage.
Afterwards I plan on adding different features such as a timer, player score, sounds and a "Hint" button.
