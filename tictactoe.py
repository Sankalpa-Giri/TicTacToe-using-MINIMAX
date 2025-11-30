import numpy as np
import math 
class Colors:
    RED = '\033[91m'      # For errors/warnings
    GREEN = '\033[92m'    # For wins
    YELLOW = '\033[93m'   # For agent win
    BLUE = '\033[94m'     # Good for information(new game, draw)
    RESET = '\033[0m'     # Resets color to default
board = [' '] * 9
#board = ['X',' ','O',' ','X',' ','O',' ',' ']
def print_board(board):
    for i in range(0,9,3):
        print(f"|{board[i]}|{board[i+1]}|{board[i+2]}|")

def check_winner(board, player):
    win_conditions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for conditions in win_conditions:
        if board[conditions[0]] == board[conditions[1]] == board[conditions[2]] == player:
            return True
    return False

def check_draw(board):
    if ' ' not in board:
        return True
    return False

def minimax(board, is_maximizing, alpha, beta):
    #check base conditions
    if check_winner(board,'X'):
        return 1
    if check_winner(board,'O'):
        return -1
    if check_draw(board):
        return 0
    
    
    #Human plays as maximizer
    if is_maximizing:
        best_score = -math.inf
        for i in range(0,9,1):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, False, alpha, beta)
                board[i] = ' '
                best_score = max(best_score, score)

                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break
        return best_score
    
    #Agent Plays as minimizer
    else:
        best_score = math.inf
        for i in range(0,9,1):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, True, alpha, beta)
                board[i] = ' '
                best_score = min(best_score, score)

                beta = min(beta, best_score)
                if alpha >= beta:
                    break
        return best_score

def best_move(board):
    best_score = math.inf
    best_move = -1
    for i in range(0,9,1):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, True, -math.inf, math.inf)
            board[i] = ' '
            if score < best_score:
                best_score = score
                best_move = i
    return best_move


def game_loop(board):
    while True:
        print_board(board)
        try:
            human_move = int(input("Make a move between 0-8: "))
            if board[human_move] != ' ':
                print(f"{Colors.RED}Cell Taken{Colors.RESET}")
                continue
            board[human_move] = 'X'
        except:
            print(f"{Colors.RED}Not a valid move.Enter Again{Colors.RESET}")
            continue
        
        #check for human win
        if check_winner(board,'X'):
            print(f"{Colors.GREEN}You Won!! It's impossible{Colors.RESET}")
            break
        if check_draw(board):
            print(f"{Colors.BLUE}It's a draw! Game Over{Colors.RESET}")
            print_board(board)
            break

        #agent moves
        agent_move = best_move(board)
        board[agent_move] = 'O'
        #check for agent win
        if check_winner(board,'O'):
            print(f"{Colors.YELLOW}Agent Won!!{Colors.RESET}")
            print_board(board)
            break
        if check_draw(board):
            print(f"{Colors.BLUE}It's a draw! Game Over{Colors.RESET}")
            break

#Game loop
print(f"{Colors.BLUE}New Game.\n1 for Human. 2 for Agent{Colors.RESET}")
choice = int(input("Enter your choice: "))
if choice == 2:
    agent_move = best_move(board)
    board[agent_move] = 'O'
    game_loop(board)

elif choice == 1:
    game_loop(board)

else:
    print(f"{Colors.RED}Invalid Choice{Colors.RESET}")
    