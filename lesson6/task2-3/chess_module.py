def is_queen_attack(pos1, pos2):
    # атакуют ли два ферзя друг друга (по горизонтали, вертикали или диагонали)
    return pos1[0] == pos2[0] or pos1[1] == pos2[1] or abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])


def check_queens_attack(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            if is_queen_attack(queens_positions[i], queens_positions[j]):
                return False
    return True