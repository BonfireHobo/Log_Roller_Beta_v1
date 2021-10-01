#  Imports
import os
from homescreen import homescreen
from levels import level

#  Clears the screen between each input (Windown/mac/linux)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#  Function that runs the game
def main():
    #  variables that deffine what screen is printed
    on = True #  Program closes when False
    playing = False #  False = Homescreen // True = Game
    won = False

    #  creates a save file or updates progress
    try:
        save = open("saved.txt", "x")
        save.write("1")
        save.close
    except FileExistsError:
        hs.update_avalible_levels_saved()

    
    
    while on:
        clear_screen()
        if not playing:   
            hs.print_homescreen()
            user_input = input("")
            if user_input.lower() == "q":
                #  Saves progress
                hs.update_save()
                #  Close program
                on = False
            else:
                playing = hs.check_input(user_input)
                selected_level = hs.get_selected_level() #  Gets selected level from homescreen
                lvl.update_selected_level(selected_level)#  and gets info for the level
            
        elif playing:
            lvl.print_level()
            won = lvl.check_win()
            if won:
                hs.update_avalible_levels()
                clear_screen()
                lvl.print_level_won() #  Changes bottom of screen
                user_input = input("")
                if user_input.lower() == "r": #  Restart the level
                    won = False
                    playing = True
                    lvl.level_info()
                elif user_input.lower()  == "q": #  Exit back to homescreen
                    won = False
                    playing = False
            else:
                user_input = input("")
                if user_input == "q": #  Close program
                    playing = False
                else:
                    lvl.move_log(user_input) #  moves the log in the level

#  Creates the homescreen and the levels
hs = homescreen()
lvl = level()

#  Checks that the file is run as main
if __name__ == "__main__":
    main()
else:
    print("This file can not be imported...")