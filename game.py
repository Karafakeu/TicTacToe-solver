import playerInput
import solverInput

first = True

def main():
    global first

    end, field = start(start=first)

    printField(field)
    
    while not end:
        inp = playerInput.playerInput(field)
        field[inp[0]][inp[1]] = 'X'
        printField(field)

        winner = checkWhoWon(field)
        if winner is not None and len(winner) == 1:
            print(winner + " has won the game!")
            end = True
            break
        elif winner is not None and len(winner) == 2:
            print("The game has ended in a tie!")
            end = True
            break

        inp = solverInput.solverInput(field)
        field[inp[0]][inp[1]] = 'O'
        printField(field)

        winner = checkWhoWon(field)
        if winner is not None and len(winner) == 1:
            print(winner + " has won the game!")
            end = True
            break
        elif winner is not None and len(winner) == 2:
            print("The game has ended in a tie!")
            end = True
            break

    input("Thanks for playing! Press enter if you wish to restart... ")

    print("Restarting...")
    first = False
    main()
    
def printField(field):
    for x in field[:-1]:
        print(x[0] + " | " + x[1] + " | " + x[2])
        print("--+---+--")
    print(field[2][0] + " | " + field[2][1] + " | " + field[2][2])
    
def start(start=False):
    if start:
        print("Welcome to Tic-Tac-Toe! The game shall begin shortly!")
        print("A small reminder on the rules: ")
        print("1. The player will play as 'X', and the computer will play as 'O'")
        print("2. Players alternate placing their marks on the board")
        print("3. The first player to get 3 in a row wins the game")
        print("4. The game is played on a 3x3 grid")
        input("Press enter to continue... ")

    field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    return False, field

def checkWhoWon(field):
    if (field[0][0] != ' ' and field[0][0] == field[1][1] == field[2][2]) or (field[0][2] != ' ' and field[0][2] == field[1][1] == field[2][0]):
        return field[1][1]

    elif (field[0][0] != ' ' and field[0][0] == field[0][1] == field[0][2]) or (field[0][0] != ' ' and field[0][0] == field[1][0] == field[2][0]):
        return field[0][0]

    elif (field[1][1] != ' ' and field[0][1] == field[1][1] == field[2][1]) or (field[1][1] != ' ' and field[1][0] == field[1][1] == field[1][2]):
        return field[1][1]

    elif (field[2][2] != ' ' and field[2][2] == field[2][1] == field[2][0]) or (field[2][2] != ' ' and field[2][2] == field[1][2] == field[0][2]):
        return field[2][2]
    
    if not any(' ' in row for row in field):
        return 'XO'
    
    return None


if __name__ == "__main__":
    main()