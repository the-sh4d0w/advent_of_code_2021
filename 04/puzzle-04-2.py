unmarked_numbers = 0


def check_board(board):
    for row in board:
        if all([cell[1] for cell in row]):
            return True
    for index in range(len(board[0])):
        if all([row[index][1] for row in board]):
            return True


with open("04/input-04.txt", "r") as f:
    data = f.read().strip()

data = data.split("\n\n")
values = data[0].split(",")
boards = [[[[cell, False] for cell in row.split()]
           for row in board.split("\n")] for board in data[1:]]

for value in values:
    found = []
    for board in boards:
        for row in board:
            for cell in row:
                if cell[0] == value:
                    cell[1] = True
        if check_board(board):
            found.append(board)
    if found and len(boards) > 1:
        for found_board in found:
            boards.remove(found_board)
    elif len(boards) == 1:
        break

for row in boards[0]:
    for cell in row:
        if not cell[1]:
            unmarked_numbers += int(cell[0])

print(unmarked_numbers * int(value))
