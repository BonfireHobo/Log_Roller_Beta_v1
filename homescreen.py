class homescreen:

    def __init__(self):
        #  logical variables
        self.width = 21
        self.height = 13
        self.selected_level = 1
        self.levels_avalible = 1

        #  Visual variables
        self.top =    [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", "L", "O", "G", " ", " ", "P", "U", "Z", "Z", "E", "L", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]]
        self.middle = [[" ", "-", "-", "-", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", ],
                       [" ", "|", "1", "|", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", ],
                       [" ", "-", "-", "-", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#", "#", " ", ]]
        self.bottom = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", "P", "R", "E", "S", "S", " ", "S", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", "T", "O", " ", " ", "S", "T", "A", "R", "T", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", "P", "R", "E", "S", "S", " ", "Q", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", "T", "O", " ", "E", "X", "I", "T", " ", " ", " ", " ", " ", " ", " ", ],
                       [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]]


    def update_avalible_levels(self):
        #  Requierments are not all level open and higest avalible level was finished
        if self.levels_avalible <= 4 and self.levels_avalible < self.selected_level + 1:
            self.levels_avalible = self.selected_level + 1

    
    def update_avalible_levels_saved(self):
        save = open("saved.txt", "r")
        self.levels_avalible = int(save.read())
        save.close()


    def update_save(self):
        save = open("saved.txt", "w")
        save.write(f"{self.levels_avalible}")
        save.close()


    def check_input(self, input):
        if input.lower() == "a" or input.lower() == "d":
            self.change_selected_level(input)
            return False
        #  Starts the selected level
        elif input.lower() == "s":
            return True

        elif input.lower() == "r":
            self.levels_avalible = 1
            self.selected_level = 1
            save = open("saved.txt", "w")
            save.write(f"{self.levels_avalible}")
            save.close()
            return False


    #  Changes variable used for visuals
    def change_selected_level(self, input):
        if input.lower() == "a" and self.selected_level - 1 >= 1:
            self.selected_level -= 1
        elif input.lower() == "d" and self.selected_level + 1 <= self.levels_avalible:
            self.selected_level += 1


    def get_selected_level(self):
        return self.selected_level


    def print_homescreen(self):
        self.change_middle()

        #  prints out the homescreen from the three lists
        for i in range(self.height):
            for j in range(self.width):
                if i <= 2:
                    print(f"{self.top[i][j]}", end= " ")
                elif i > 2 and i < 6:
                    print(f"{self.middle[i - 3][j]}", end= " ")
                else:
                    print(f"{self.bottom[i - 6][j]}", end= " ")
            print()


    #  Changes visuals for avalible levels and witch level is selected
    def change_middle(self):
        #  Avalible leves loop
        cord_add = 1
        for i in range(1, 6):
            if i <= self.levels_avalible:
                self.middle[1][i + cord_add] = i
            else:
                self.middle[1][i + cord_add] = "#"
            cord_add += 3

        #  Selected levels loop
        for i in range(1, 6):
            for j in range(i*4-3, i*4):
                if i == self.selected_level:
                    self.middle[0][j] = "-"
                    self.middle[2][j] = "-"
                else:
                    self.middle[0][j] = "#"
                    self.middle[2][j] = "#"
            for k in range(i*4-3, i*4, 2):
                if i == self.selected_level:
                    self.middle[1][k] = "|"
                else:
                    self.middle[1][k] = "#"