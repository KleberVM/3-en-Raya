def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")

def evaluate(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    result = evaluate(board)
    
    if result is not None:
        if result == 'O':
            return 1
        elif result == 'X':
            return -1
        else:
            return 0
    
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth+1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth+1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Bienvenido al juego de 3 en raya!")
    player = input("""
    Elija a quien ayudara el automata :
        jugador 1 o jugador 2 :
""")
    
    if player == '2':
        is_player_turn = True
    elif player == '1':
        is_player_turn = False
    else:
        print("Jugador no válido. Por favor, elija 'X' o 'O'")
        return
    
    while True:
        print_board(board)
        if is_player_turn:
            row, col = map(int, input("Ingrese la posición (fila y columna) que desea marcar separados por un espacio: ").split())
            if board[row][col] != ' ':
                print("Posición ocupada. Intente de nuevo.")
                continue
            board[row][col] = 'X'
        else:
            print("Calculando mejor movimiento para O...")
            row, col = find_best_move(board)
            print(f"La computadora marca en la posición: ({row}, {col})")
            row, col = map(int, input("Ingrese la posición (fila y columna) que desea marcar separados por un espacio: ").split())
            board[row][col] = 'O'
        
        if evaluate(board) is not None:
            print_board(board)
            if is_player_turn:
                print("¡Jugador 2 ha ganado!")
            else:
                print("¡Jugador 1 ha ganado!.")
            break
        
        if is_board_full(board):
            print_board(board)
            print("¡Empate!")
            break
        
        is_player_turn = not is_player_turn

play_game()