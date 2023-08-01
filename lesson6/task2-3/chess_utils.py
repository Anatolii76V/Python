def is_queen_attack(pos1, pos2):
    row1, col1 = pos1
    row2, col2 = pos2

    return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)
