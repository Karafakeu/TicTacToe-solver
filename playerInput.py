def playerInput(field, inp=None):
    if inp == None:
        inp = input("Enter your move: ")

    inp = str(inp)

    if len(inp) != 4:
        inp = usageSize(field)
        return inp
    
    try:
        inp = [int(x) for x in inp.split(",")]
    except ValueError:
        inp = usageType(field)

    inp[0] -= 1
    inp[1] -= 1

    inp[0], inp[1] = inp[1], inp[0]

    if inp[0] not in range(0, 3) or inp[1] not in range(0, 3):
        inp = usageNumber(field)

    if field[inp[0]][inp[1]] != ' ':
        inp = usageRepeat(field)

    return inp

def usageSize(field):
    print("Enter your move in the format 'row number, column number'!")

    inp = playerInput(field)
    return inp

def usageType(field):
    print("Entered move must contain numbers!")

    inp = playerInput(field)
    return inp

def usageNumber(field):
    print("Entered input extends outside of the playing field, please input a valid number!")
    
    inp = playerInput(field)
    return inp

def usageRepeat(field):
    print("Entered move has already been made, please input a new move!")
    
    inp = playerInput(field)
    return inp