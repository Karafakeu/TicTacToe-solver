import random
from game import checkWhoWon

def minimax(field, depth, alpha, beta, isMaximizing):
    winner = checkWhoWon(field)
    if winner == 'X':
        return -10 + depth # player won, we want to prio later losses

    if winner == 'O':
        return 10 - depth # computer won, we want to prio sooner wins
    
    if winner == 'XO':
        return 0 # tie
    
    # computer move
    if isMaximizing:
        bestScore = -float("inf")
        for x in range(3):
            for y in range(3):
                if field[x][y] == ' ':
                    field[x][y] = 'O'
                    score = minimax(field, depth + 1, alpha, beta, False)
                    field[x][y] = ' '
                    bestScore = max(score, bestScore)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return bestScore

    # player move
    else:
        bestScore = float("inf")
        for x in range(3):
            for y in range(3):
                if field[x][y] == ' ':
                    field[x][y] = 'X'
                    score = minimax(field, depth + 1, alpha, beta, True)
                    field[x][y] = ' '
                    bestScore = min(score, bestScore)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
            if beta <= alpha:
                break
        return bestScore

def solverInput(field):
    print("Computer is thinking... ")
    bestScore = -float("inf")
    move = (-1, -1)

    for x in range(3):
        for y in range(3):
            if field[x][y] == ' ':
                field[x][y] = 'O'
                score = minimax(field, 0, -float("inf"), float("inf"), False)
                field[x][y] = ' '

                if score > bestScore:
                    bestScore = score
                    move = (x, y)

    if move == (-1, -1):
        move = random.choice([(x, y) for x in range(3) for y in range(3) if field[x][y] == ' '])

    return move