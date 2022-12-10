import numpy as np


class Knot:

    def __init__(self, name, x, y):
        self.name: str = name
        self.x = x
        self.y = y
        # self.next_knot = None
        # self.previous_knot = previous_knot


move_directions = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0)
}


class Rope:

    def __init__(self):
        self.knots = []
        self.diagonal_move = {}

        for i in range(10):
            # if i == 0:
            #     previous_knot = None
            # else:
            #     previous_knot = self.knots[i - 1]

            knot = Knot(str(i), 0, 0)
            self.knots.append(knot)
            self.diagonal_move[i] = []

        # puts head at the start of the rope list
        self.knots.reverse()


def main(file):
    with open(file) as input_file:
        rope = Rope()
        visited_positions = set()

        print("== Initial State ==")
        print_grid(rope, 6)

        for line in input_file:
            move = line.rstrip('\n').split(' ')
            direction = move[0]
            occurrence = move[1]

            print(f"== {direction} {occurrence} ==\n")
            make_moves(rope, direction, int(occurrence), visited_positions)

        print("== Visited Positions  ==")
        print_visited_positions(visited_positions, 6, 5)

        print('Total visited positions:', len(visited_positions))


def make_moves(rope: Rope, direction, occurrence: int, visited_positions):

    for n in range(occurrence):

        # current_knot = rope.knots[i]

        apply_move(rope.knots[0], direction)

        for i in range(1, len(rope.knots)):
            previous_knot = rope.knots[i - 1]
            next_knot = rope.knots[i]

            # print(previous_knot.name, next_knot.name)

            x_distance = previous_knot.x - next_knot.x
            y_distance = previous_knot.y - next_knot.y

            if x_distance == 0 and y_distance == 0:
                continue

            if abs(x_distance) == 1 and abs(y_distance) == 1:
                # save the position of the head when moved diagonally to use to update tail
                rope.diagonal_move[i].clear()
                rope.diagonal_move[i - 1] = [Knot(previous_knot.name, previous_knot.x, previous_knot.y)]
            else:
                if len(rope.diagonal_move[i - 1]) > 0:
                    # print(f'diagonal knot {i}')
                    move = rope.diagonal_move[i].pop()
                    next_knot = Knot(move.name, move.x, move.y)
                    rope.knots[i] = next_knot
                else:
                    # print(f'apply move knot {i}')
                    apply_move(next_knot, direction)

            if i == len(rope.knots) - 1:
                visited_positions.add((next_knot.x, next_knot.y))

        print_grid(rope, 6)


def print_grid(rope: Rope, grid_size):
    grid = ""

    for y in range(grid_size):
        row = ""
        for x in range(grid_size):

            knots = rope.knots

            knot_printed = False

            for knot in knots:
                if knot.x == x and knot.y == y:
                    row += knot.name + " "
                    knot_printed = True
                    break

            if not knot_printed:
                if x == 0 and y == 0:
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


def apply_move(position: Knot, direction):
    position.x += move_directions[direction][0]
    position.y += move_directions[direction][1]


if __name__ == '__main__':
    main('basic-input.txt')
