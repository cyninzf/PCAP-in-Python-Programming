# 3.7.1.1 Lists in advanced applications

squares = [x**2 for x in range(10)]
print(squares,"\n")

twos = [2**i for i in range(8)]
print(twos,"\n")

odds = [x for x in squares if x % 2 !=0]
print(odds, "\n")

evens =[]

for x in squares:
    if x % 2 == 0:
        evens.append(x)
print(evens, "\n")


# 3.7.1.2 Lists in advanced applications | Arrays
# Lists in lists: two-dimensional arrays

EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)

