The program displays a quote of the day from famous people.
Quotes are stored in two files: quotes_en.txt (for English quotes) and quotes_ru.txt (for Russian quotes).

The current quote is saved in the phrase_state.json file and remains unchanged until the end of the day. Previously used quotes are stored in the used_phrases.json file. These two JSON files are created automatically when the main program is run.

You can use PyInstaller to compile the program into an executable file. In this case, the quote files must be located in the same folder as the executable.

A shortcut to the executable can be placed in the system's startup folder. When the computer is turned on, a window with the quote of the day will appear.