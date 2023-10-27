"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x = 0
    o = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                x += 1
            elif board[row][col] == O:
                o += 1
    
    if x == o:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    options = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                options.add((row, col))

    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if board[action[0]][action[1]] != EMPTY:
        raise Exception('invalid move')
    
    newboard = []
    for row in board:
        newboard.append(row.copy())

    newboard[action[0]][action[1]] = player(board)
    return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    # check horizontal
    for row in board:
        if len(set(row)) == 1 and row[0] != EMPTY:
            return row[0]

    # check vertical
    for x in range(3):
        if (
            len({board[0][x], board[1][x], board[2][x]}) == 1
            and board[0][x] != EMPTY
        ):
            return board[0][x]

    # check diagonal
    if (
        len({board[0][0], board[1][1], board[2][2]}) == 1
        and board[0][0] != EMPTY
    ):
        return board[0][0]
    if len({board[0][2], board[1][1], board[2][0]}) == 1:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board):
        return True
    
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == X:
        return 1
    if result == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None
    
    moves = []

    for move in actions(board):
        moves.append((alphabeta(
            result(board, move),
            -2,
            2,
            False if player(board) == X else True
        ), move))
    
    if player(board) == X:
        moves.sort(reverse=True, key=lambda e: e[0])
    else:
        moves.sort(key=lambda e: e[0])

    return moves[0][1]


def alphabeta(board, alpha, beta, isMaxi):
    if terminal(board):
        return utility(board)
    
    if isMaxi:
        record = -2
        for move in actions(board):
            record = max(record, alphabeta(
                result(board, move),
                alpha,
                beta,
                False))
            if record > beta:
                break
            alpha = max(alpha, record)
        return record
    else:
        record = 2
        for move in actions(board):
            record = min(record, alphabeta(
                result(board, move),
                alpha,
                beta,
                True
            ))
            if record < alpha:
                break
            beta = min(beta, record)
        return record
