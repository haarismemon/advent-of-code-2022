import numpy as np


class Knot:

    def __init__(self, name, x, y):
        self.name: str = name
        self.x = x
        self.y = y


class Rope:

    def __init__(self):
        self.knots = []

        for i in range(10):
            knot = Knot(str(i), 0, 0)
            self.knots.append(knot)


move_directions = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


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
        print_visited_positions(visited_positions, 6)

        print('Total visited positions:', len(visited_positions))


def make_moves(rope: Rope, direction, occurrence: int, visited_positions):
    for n in range(occurrence):

        apply_move(rope.knots[0], direction)

        for i in range(1, len(rope.knots)):
            previous_knot = rope.knots[i - 1]
            next_knot = rope.knots[i]

            x_distance = previous_knot.x - next_knot.x
            y_distance = previous_knot.y - next_knot.y

            if (abs(x_distance) > 1) or (abs(y_distance) > 1):
                next_knot.x += np.sign(x_distance)
                next_knot.y += np.sign(y_distance)

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
                    if knot.name == "0":
                        row += "H "
                    else:
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


def print_visited_positions(visited_positions, grid_size):
    grid = ""

    for y in range(grid_size):
        row = ""
        for x in range(grid_size):

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
