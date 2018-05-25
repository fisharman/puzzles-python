# https://leetcode.com/problems/n-queens/description/

def check_around(n, board, x, y, ):
    # check side to side (across y)
    for spot in range(y - 1, -1):
        if board[x][spot] == 'Q':
            return False

    for spot in range(y + 1, n):
        if board[x][spot] == 'Q':
            return False

    # check up and down (across x)
    for spot in range(x - 1, - 1):
        if board[spot][y] == 'Q':
            return False

    for spot in range(x + 1, n):
        if board[spot][y] == 'Q':
            return False

    # check diagonal
    # NW x-i, y-i
    for i in range(1, min(x, y)):
        if board[x - i][y - 1] == 'Q':
            return False

    # NE x+i, y-i
    for i in range(1, n + 1 - max(x, y)):
        if board[x + i][y - i] == 'Q':
            return False

    # SW x-i, y+1
    for i in range(1, min(x, n - y)):
        if board[x - i][y + i] == 'Q':
            return False

            # SE x+i, y+1
    for i in range(1, min(n - x, n - y)):
        if board[x + i][y + i] == 'Q':
            return False

    return True


def fill_queen(n, board, x, y):
    if x > n:
        if y > n:
        # print out list
        else:
            x = 0
            y += 1
    else:
        x += 1

    if check_around(n, board, x, y):
        board[x][y] = 'Q'

    fill_queen()

    fill_queen(n, board, )


def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    board = [['.' for _ in n] for _ in n]

    if check_around(n, board, 0, 0):
        board[0][0] = 'Q'
        check_around(n, board, 0, 1)