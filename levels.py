class level:
    
    def __init__(self):
        #  Logic variables
        self.screen_width = 21
        self.screen_height = 13
        self.level_size = 9
        self.current_level = 1
        self.level = [[" " for _ in range(self.level_size)] for _ in range(self.level_size)]
        self.log_pos = [[8], [0]]
        self.start_pos = [[8], [0]]
        self.end_pos = [[0], [8]]

        #  Visual variables
        self.top = [[" ", " ", " ", " ", " ", " ", " ", "L", "E", "V", "E", "L", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "]]

        self.bottom = [[" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
                       [" ", "R", "E", "S", "T", "A", "R", "T", " ", "R", " ", " ", " ", " ", "E", "X", "I", "T", " ", "Q", " "]]

        self.bottom_win = [[" ", " ", " ", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", " ", " ", " "],
                           [" ", "Y", "O", "U", " ", "W", "O", "N", " ", " ", " ", "P", "R", "E", "S", "S", " ", "R", "/", "Q", " "]]    

    #  Matches selected level with whats chosen in homescreen
    def update_selected_level(self, selected):
        self.current_level = selected
        self.level_info()
    

    #  Update the back end info
    def level_info(self):
        if self.current_level == 1:
            self.start_pos = [[8], [0]]
            self.end_pos = [[0], [8]]
            self.log_pos = [[8], [0]] 
            self.top[0][13] = "1"

        elif self.current_level == 2:
            self.start_pos = [[8], [4]]
            self.end_pos = [[4], [4]]
            self.log_pos = [[8], [4]]
            self.top[0][13] = "2"   
            
        elif self.current_level == 3:
            self.start_pos = [[8], [0]]
            self.end_pos = [[0], [4]]
            self.log_pos = [[8], [0]]
            self.top[0][13] = "3" 

        elif self.current_level == 4:
            self.start_pos = [[8], [0]]
            self.end_pos = [[3], [4]]
            self.log_pos = [[8], [0]] 
            self.top[0][13] = "4"

        elif self.current_level == 5:
            self.start_pos = [[2], [2]]
            self.end_pos = [[6], [6]]
            self.log_pos = [[2], [2]] 
            self.top[0][13] = "5"

    #  Updates the visuals for the level
    def update_level(self):
        #  Clear level for old walls
        self.level = [[" " for _ in range(self.level_size)] for _ in range(self.level_size)]

        #  Adds graphic for start pos and end pos
        self.level[self.start_pos[0][0]][self.start_pos[1][0]] = "-"
        self.level[self.end_pos[0][0]][self.end_pos[1][0]] = "+"

        #  Cordinats for the walls in each level // wall_cords[y][x]
        if self.current_level == 1:
            wall_cords = [[], [6, 7, 8], [0, 1, 2, 3, 4], [4], [4], [1, 5, 6, 7], [1], [1, 2, 3, 4, 5, 6, 7], [1]]
        elif self.current_level == 2:
            wall_cords = [[4, 7], [7], [3, 4, 5, 7], [2], [8], [2, 3, 4], [2, 5, 6 ,7], [0, 2], []]
        elif self.current_level == 3:
            wall_cords = [[2, 5], [], [2, 3, 6], [], [1, 4], [3], [6, 8], [1, 4], []]
        elif self.current_level == 4:
            wall_cords = [[2], [5], [1, 3, 4, 5, 8], [6], [2], [0, 5, 8], [2], [4, 6], []]
        elif self.current_level == 5:
            wall_cords = [[7, 8], [1, 4], [5], [1, 7], [5], [1, 2, 3, 8], [4, 5], [], [1, 2 ,6]]

        #  add walls into the level
        for i in range(self.level_size):
            for j in wall_cords[i]:
                self.level[i][j] = "#"


    def move_log(self, input): 
        y, x = 0, 1
        if input.lower() == "w":            
            if (len(self.log_pos[y]) == 1 and len(self.log_pos[x]) == 1):
                self.log_pos[y][0] -= 2
                self.log_pos[y].append(self.log_pos[y][0] + 1)

                if self.log_pos[y][0] <= -1:
                    self.log_pos[y][0] += 2
                    self.log_pos[y].pop()
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[y][0] += 2
                    self.log_pos[y].pop()
                elif self.level[self.log_pos[y][1]][self.log_pos[x][0]] == "#":
                    self.log_pos[y][0] += 2
                    self.log_pos[y].pop()
            
            elif len(self.log_pos[y]) == 1 and len(self.log_pos[x]) == 2:
                self.log_pos[y][0] -= 1

                if self.log_pos[y][0] <= -1:
                    self.log_pos[y][0] += 1
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[y][0] += 1
                elif self.level[self.log_pos[y][0]][self.log_pos[x][1]] == "#": 
                    self.log_pos[y][0] += 1

            elif len(self.log_pos[y]) == 2 and len(self.log_pos[x]) == 1:
                self.log_pos[y][0] -= 1
                self.log_pos[y].pop()

                if self.log_pos[y][0] <= -1:
                    self.log_pos[y][0] += 1
                    self.log_pos[y].append(self.log_pos[y][0] + 1)
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[y][0] += 1
                    self.log_pos[y].append(self.log_pos[y][0] + 1)

        elif input.lower() == "a":
            if (len(self.log_pos[y]) == 1 and len(self.log_pos[x]) == 1):
                self.log_pos[x][0] -= 2
                self.log_pos[x].append(self.log_pos[x][0] + 1)

                if self.log_pos[x][0] <= -1:
                    self.log_pos[x][0] += 2
                    self.log_pos[x].pop()
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[x][0] += 2
                    self.log_pos[x].pop()
                elif self.level[self.log_pos[y][0]][self.log_pos[x][1]] == "#":
                    self.log_pos[x][0] += 2
                    self.log_pos[x].pop()

            elif len(self.log_pos[y]) == 1 and len(self.log_pos[x]) == 2:
                self.log_pos[x][0] -= 1
                self.log_pos[x].pop()

                if self.log_pos[x][0] <= -1 :
                    self.log_pos[x][0] += 1
                    self.log_pos[x].append(self.log_pos[x][0] + 1)
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[x][0] += 1
                    self.log_pos[x].append(self.log_pos[x][0] + 1)

            elif len(self.log_pos[y]) == 2 and len(self.log_pos[x]) == 1:
                self.log_pos[x][0] -= 1

                if self.log_pos[x][0] <= -1 :
                    self.log_pos[x][0] += 1
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[x][0] += 1
                elif self.level[self.log_pos[y][1]][self.log_pos[x][0]] == "#": 
                    self.log_pos[x][0] += 1

        elif input.lower() == "s":
            if (len(self.log_pos[y]) == 1 and len(self.log_pos[x]) == 1):
                self.log_pos[y][0] += 1
                self.log_pos[y].append(self.log_pos[y][0] + 1)

                if self.log_pos[y][1] >= self.level_size:
                    self.log_pos[y][0] -= 1
                    self.log_pos[y].pop()
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[y][0] -= 1
                    self.log_pos[y].pop()
                elif self.level[self.log_pos[y][1]][self.log_pos[x][0]] == "#":
                    self.log_pos[y][0] -= 1
                    self.log_pos[y].pop()

            elif len(self.log_pos[y]) == 1 and len(self.log_pos[x]) == 2:
                self.log_pos[y][0] += 1

                if self.log_pos[y][0] >= self.level_size:
                    self.log_pos[y][0] -= 1
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[y][0] -= 1
                elif self.level[self.log_pos[y][0]][self.log_pos[x][1]] == "#": 
                    self.log_pos[y][0] -= 1

            elif len(self.log_pos[y]) == 2 and len(self.log_pos[x]) == 1:
                self.log_pos[y][0] += 2
                self.log_pos[y].pop()

                if self.log_pos[y][0] >= self.level_size:
                    self.log_pos[y][0] -= 2
                    self.log_pos[y].append(self.log_pos[y][0] + 1)
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[y][0] -= 2
                    self.log_pos[y].append(self.log_pos[y][0] + 1)

        elif input.lower() == "d":
            if (len(self.log_pos[y]) == 1 and len(self.log_pos[x]) == 1):
                self.log_pos[x][0] += 1
                self.log_pos[x].append(self.log_pos[x][0] + 1)

                if self.log_pos[x][1] >= self.level_size:
                    self.log_pos[x][0] -= 1
                    self.log_pos[x].pop()
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[x][0] -= 1
                    self.log_pos[x].pop()
                elif self.level[self.log_pos[y][0]][self.log_pos[x][1]] == "#":
                    self.log_pos[x][0] -= 1
                    self.log_pos[x].pop()

            elif len(self.log_pos[y]) == 1 and len(self.log_pos[x]) == 2:
                self.log_pos[x][0] += 2
                self.log_pos[x].pop()

                if self.log_pos[x][0] >= self.level_size:
                    self.log_pos[x][0] -= 2
                    self.log_pos[x].append(self.log_pos[x][0] + 1)
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[x][0] -= 2
                    self.log_pos[x].append(self.log_pos[x][0] + 1)

            elif len(self.log_pos[y]) == 2 and len(self.log_pos[x]) == 1:
                self.log_pos[x][0] += 1

                if self.log_pos[x][0] >= self.level_size :
                    self.log_pos[x][0] -= 1
                elif self.level[self.log_pos[y][0]][self.log_pos[x][0]] == "#": 
                    self.log_pos[x][0] -= 1
                elif self.level[self.log_pos[y][1]][self.log_pos[x][0]] == "#": 
                    self.log_pos[x][0] -= 1

        #  Moves log back to start position
        elif input.lower() == "r":
            self.level_info()

    #  Checks if log is standing on the end position
    def check_win(self):
        return True if self.log_pos == self.end_pos else False   

    def print_level_won(self):
        for i in range(self.screen_height):
                for j in range(self.screen_width):
                    if i <= 1:
                        print(f"{self.top[i][j]}", end= " ")
                    elif i >= 2 and i <= 10 and j >= 6 and j <= 14:
                        print(f"{self.level[i - 2][j - 6]}", end= " ")
                    elif i >= 11:
                        print(f"{self.bottom_win[i - 11][j]}", end= " ")
                    elif i >= 2 and i <= 10 and (j == 5 or j == 15):
                        print("#", end= " ")
                    else:
                        print(" ", end= " ")
                print()

    def print_level(self):
            self.update_level()
            for i in range(len(self.log_pos[0])):
                for j in range(len(self.log_pos[1])):
                    self.level[self.log_pos[0][i]][self.log_pos[1][j]] = "@"
            
            for i in range(self.screen_height):
                for j in range(self.screen_width):
                    if i <= 1:
                        print(f"{self.top[i][j]}", end= " ")
                    elif i >= 2 and i <= 10 and j >= 6 and j <= 14:
                        print(f"{self.level[i - 2][j - 6]}", end= " ")
                    elif i >= 11:
                        print(f"{self.bottom[i - 11][j]}", end= " ")
                    elif i >= 2 and i <= 10 and (j == 5 or j == 15):
                        print("#", end= " ")
                    else:
                        print(" ", end= " ")
                print()