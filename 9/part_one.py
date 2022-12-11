class Knot:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rope:

    def __init__(self):
        self.h = Knot(0, 0)
        self.t = Knot(0, 0)


move_directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


def main(file):
    with open(file) as input_file:

        rope = Rope()
        visited_positions = set()

        diagonal_move = []

        for line in input_file:
            move = line.rstrip('\n').split(' ')
            direction = move[0]
            occurrence = move[1]

            make_moves(rope, direction, int(occurrence), visited_positions, diagonal_move)

        print('Total visited positions:', len(visited_positions))


def make_moves(rope: Rope, direction, occurrence: int, visited_positions, diagonal_move):

    for n in range(occurrence):
        apply_move(rope.h, direction)

        x_distance = rope.h.x - rope.t.x
        y_distance = rope.h.y - rope.t.y

        if abs(x_distance) <= 1 and abs(y_distance) <= 1:
            # save the position of the head when moved diagonally to use to update tail
            diagonal_move.clear()
            diagonal_move.append(Knot(rope.h.x, rope.h.y))
        else:
            if len(diagonal_move) > 0:
                move = diagonal_move.pop()
                rope.t = Knot(move.x, move.y)
            else:
                apply_move(rope.t, direction)

            visited_positions.add((rope.t.x, rope.t.y))


def apply_move(position: Knot, direction):
    position.x += move_directions[direction][0]
    position.y += move_directions[direction][1]


if __name__ == '__main__':
    main('input.txt')
