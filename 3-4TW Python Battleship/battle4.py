import copy
import os
os.system('clear')


def shooting(grid, row, column):  # lövés
    hit = 0
    if grid[row][column] == 0:
        grid[row][column] = "#"
    elif grid[row][column] == "X":
        grid[row][column] = "H"
        hit = 1
    return hit


def ship_placement(grid, row, column, direction, length):  # hajók lerakása
    k = 0
    if direction == 1:
        while k < length:
            grid[row + k][column] = "X"
            k += 1
    elif direction == 0:
        while k < length:
            grid[row][column + k] = "X"
            k += 1
    grid_preview(grid)
    return length


def fog_of_war(grid):  # játék közben lathato palya
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#" or grid[i][j] == "H":
                print(grid[i][j], end=" ")
            else:
                print(0, end=" ")
        print()


def grid_preview(grid):  # mindent felfedo palya
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print()


def out_of_grid(grid, row, column, direction, length):  # ne lehessen palyan kivulre rakni
    if direction == 1:
        if row < 0 or row > len(
                grid) or row + length > len(grid) or column < 0 or column > len(grid[0]):
            all_good = 0
            print("Please enter valid parameters!\n")
        else:
            all_good = 1
    elif direction == 0:
        if row < 0 or row > len(grid) or column < 0 or column > len(
                grid[0]) or column + length > len(grid[0]):
            all_good = 0
            print("Please enter valid parameters!\n")
        else:
            all_good = 1
    else:
        all_good = 0
        print("Direction error! 1 is vertical, 0 is horizontal.")
    return all_good


def print_all():  # játékkép printelése

    print("\nFirst players life:", life1)
    print("Second players life:", life2)
    print("Turns left:", turn)
    print("\nFirst player:")
    fog_of_war(grid1)
    print("\nSecond player:")
    fog_of_war(grid2)
    print()


# relatív hajóelhelyezés csekkolása
def placement_check(grid, row, column, direction, length):
    all_good = 1
    # vizszintes
    if direction == 0:
        if row == 0:
            for i in grid[row:row + 2]:
                if column == 0 and all_good == 1:
                    for j in i[column:column + length + 1]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
                elif all_good == 1:  # column > 0
                    for j in i[column - 1:column + length + 1]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
        else:  # row > 0
            for i in grid[row - 1:row + 2]:
                if column == 0 and all_good == 1:
                    for j in i[column:column + length + 1]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
                elif all_good == 1:  # column > 0
                    for j in i[column - 1:column + length + 1]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
    # fuggoleges
    if direction == 1:
        if row == 0:
            for i in grid[row:row + length + 1]:
                if column == 0 and all_good == 1:
                    for j in i[column:column + 2]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
                elif all_good == 1:  # column > 0
                    for j in i[column - 1:column + 2]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
        else:  # row > 0
            for i in grid[row - 1:row + length + 1]:
                if column == 0 and all_good == 1:
                    for j in i[column:column + 2]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
                elif all_good == 1:  # column > 0
                    for j in i[column - 1:column + 2]:
                        if grid[grid.index(i)][i.index(j)] == "X":
                            print("Keep your distance!")
                            all_good = 0
    return all_good


#ITT KEZDODIK##################################
print('\nWelcome to DKP Battleship Game!\n')
try:
    row = int(input('Size of the grid? \n'))
except ValueError:
    print("Please enter a valid parameter!\n")

life1 = 0  # erteket kell kapniuk, mert kesobb csak +=el szerepel
life2 = 0
column = row
TURN = 20

# hajok kiosztasa    indexek jelolik a hajok hosszat(length), ertekek
# pedig a darabszamot
ships5 = (0, 0, 2)
ships6 = (0, 0, 2, 1)
ships7 = (0, 0, 2, 2)
ships8 = (0, 0, 3, 2)
ships9 = (0, 0, 2, 2, 0, 1)

if row == 5:
    ships = ships5
elif row == 6:
    ships = ships6
elif row == 7:
    ships = ships7
elif row == 8:
    ships = ships7
elif row == 9:
    ships = ships9

# palyak generalasa
grid1 = [0] * row
i = 0
for i in range(row):
    grid1[i] = [0] * column
grid2 = copy.deepcopy(grid1)

##########################################

# hajo elhelyezes
for i in range(len(ships)):
    k = 1   # aktualis meretu hajo darabszamat koveto valtozo
    while k <= ships[i]:
        length = i
        all_good = 0
        while all_good == 0:
            # P1
            print("First player:")
            try:
                row_ship = int(input("\nRow of ship? \n")) - 1
                column_ship = int(input("\nColumn of ship? \n")) - 1
                direction = int(
                    input("\nDirection of ship? (1 is vertical, 0 is horizontal.)\n"))
            except ValueError:
                print("Please enter a valid parameter!\n")
                continue
            all_good = out_of_grid(
                grid1, row_ship, column_ship, direction, length)
            if all_good == 0:
                continue
            all_good = placement_check(
                grid1, row_ship, column_ship, direction, length)
            if all_good == 0:
                continue
            life1 += ship_placement(grid1, row_ship,
                                    column_ship, direction, length)
        k += 1
# P2
os.system('clear')
for i in range(len(ships)):
    k = 1
    while k <= ships[i]:
        length = i
        all_good = 0
        while all_good == 0:
            print("\nSecond player:")
            try:
                row_ship = int(input("\nRow of ship? \n")) - 1
                column_ship = int(input("\nColumn of ship? \n")) - 1
                direction = int(input("\nDircetion of ship? \n"))
            except ValueError:
                print("Please enter a valid parameter!\n")
                continue
            all_good = out_of_grid(
                grid2, row_ship, column_ship, direction, length)
            if all_good == 0:
                continue
            all_good = placement_check(
                grid2, row_ship, column_ship, direction, length)
            if all_good == 0:
                continue
            life2 += ship_placement(grid2, row_ship,
                                    column_ship, direction, length)
        k += 1

os.system('clear')
while life1 > 0 and life2 > 0 and turn > 0:  # itt kezdődik a csata
    print_all()
# shooting
# P1
    all_good = 0
    while all_good == 0:
        print("\nFirst player shoots:\n")
        try:
            row_ship = int(input("Row of target?\n")) - 1
            column_ship = int(input("Column of target?\n")) - 1
        except ValueError:
            print("\nPlease enter a valid parameter!\n")
            continue
        all_good = out_of_grid(grid1, row_ship, column_ship, 1, 0)
        if all_good == 0:
            continue
        life2 = life2 - shooting(grid1, row_ship, column_ship)

        os.system('clear')
        print_all()
# P2
    all_good = 0
    while all_good == 0:
        print("\nSecond player shoots:\n")
        try:
            row_ship = int(input("Row of target?\n")) - 1
            column_ship = int(input("Column of target?\n")) - 1
        except ValueError:
            print("\nPlease enter a valid parameter!\n")
            continue
        all_good = out_of_grid(grid2, row_ship, column_ship, 1, 0)
        if all_good == 0:
            continue
        life1 = life1 - shooting(grid2, row_ship, column_ship)

    os.system('clear')
    turn -= 1

print_all()
if life2 == 0:
    print("\nFirst player wins!")
elif life1 == 0:
    print("\nSecond player wins!")
elif turn == 0:
    print("\nGame fucking over, mate!")
