class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tuple = (x, y)


move_directions = {
    "U": Position(0, 1),
    "D": Position(0, -1),
    "R": Position(1, 0),
    "L": Position(-1, 0)
}


class Rope:

    def __init__(self):
        self.h = Position(0, 0)
        self.t = Position(0, 0)


def main(file):
    with open(file) as input_file:

        head_and_tail = Rope()
        visited_positions = {}
        add_to_history(visited_positions, head_and_tail.t)

        print("== Initial State ==")
        print_grid(head_and_tail, 0, 0, 6)

        for line in input_file:
            move = line.rstrip('\n').split(' ')
            direction = move[0]
            occurrence = move[1]

            print(f"== {direction} {occurrence} ==\n")
            make_moves(head_and_tail, move_directions[direction], int(occurrence), visited_positions)

        print("== Visited Positions  ==")
        print_visited_positions(visited_positions, 6, 5)

        for (position, occurrence) in visited_positions.items():
            print(position[0], position[1], occurrence)

        print('Total visited positions:', len(visited_positions.keys()))


def make_moves(rope: Rope, move: Position, occurrence: int, visited_positions):
    diagonal_move: Position = None

    for n in range(occurrence):
        apply_move(rope.h, move)

        x_distance = rope.h.x - rope.t.x
        y_distance = rope.h.y - rope.t.y

        if x_distance == 0 and y_distance == 0:
            continue

        if diagonal_move is not None:
            rope.t = Position(diagonal_move.x, diagonal_move.y)
            add_to_history(visited_positions, rope.t)
            diagonal_move = None
        elif abs(x_distance) == 1 and abs(y_distance) == 1:
            # save the position of the head when moved diagonally to use to update tail
            diagonal_move = Position(rope.h.x, rope.h.y)
        elif abs(x_distance) > 1 or abs(y_distance) > 1:
            apply_move(rope.t, move)
            add_to_history(visited_positions, rope.t)

        # print_grid(head_and_tail, 270, 100, 6)


def apply_move(position: Position, move: Position):
    position.x += move.x
    position.y += move.y


def add_to_history(position_history, position):
    copy_position = (position.x, position.y)

    if copy_position in position_history:
        position_history[copy_position] = position_history[copy_position] + 1
    else:
        position_history[copy_position] = 1


def print_grid(head_and_tail: Rope, start_x, start_y, grid_size):
    grid = ""

    for y in range(head_and_tail.t.y - grid_size, head_and_tail.t.y + grid_size):
        row = ""
        for x in range(head_and_tail.t.x - grid_size, head_and_tail.t.x + grid_size):

            if head_and_tail.h.x == x and head_and_tail.h.y == y:
                row += "H "

            elif head_and_tail.t.x == x and head_and_tail.t.y == y:
                row += "T "

            elif x == 0 and y == 0:
                row += "s "

            else:
                row += "- "

        grid = row + '\n' + grid

    print(grid)


def print_visited_positions(visited_positions, i, j):
    grid = ""

    for y in range(j):
        row = ""
        for x in range(i):

            if (x, y) in visited_positions:
                row += "# "

            elif x == 0 and y == 0:
                row += "s "

            else:
                row += "- "

        grid = row + '\n' + grid

    print(grid)


if __name__ == '__main__':
    main('input.txt')
    # main('basic-input.txt')
