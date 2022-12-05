import re


def main():
    with open('input.txt') as input_file:
        stacks = {}
        rows = []
        instructions = []

        separate_stacks_and_instructions(input_file, instructions, rows)
        initialise_stacks(rows, stacks)
        arrange_initial_stacks(rows, stacks)

        print('start:', stacks)
        perform_moves(instructions, stacks)
        print('end:', stacks)

        final_result = ""
        for stacks in stacks.values():
            final_result += str(stacks[-1]).lstrip('[').rstrip(']')

        print('\nfinal result:', final_result)


def separate_stacks_and_instructions(input_file, instructions, rows):
    for line in input_file:
        instruction = line.rstrip('\n')

        if 'move' not in line and line != '\n':
            row = instruction.split(' ')
            rows.append(row)
        else:
            if line != '\n':
                instructions.append(instruction)


def initialise_stacks(rows, stacks):
    total_num_stacks = get_total_num_stacks(rows)
    rows.reverse()
    for n in range(1, total_num_stacks):
        stacks[n] = []


def arrange_initial_stacks(rows, stacks):
    for row in rows:
        col = 1
        whitespace_count = 0

        for i in row:
            if '[' in i:
                stacks[col].append(i)
                col += 1
            elif i == '':
                whitespace_count += 1
                if whitespace_count == 4:
                    col += 1
                    whitespace_count = 0


def get_total_num_stacks(rows):
    numbers_row = rows.pop()
    index = -1
    if numbers_row[index] == '':
        index = -2

    return int(numbers_row[index]) + 1


def perform_moves(instructions, stacks):
    for move in instructions:
        p = "^move (\d*) from (\d*) to (\d*)$"

        result = re.search(p, move)

        occurrences = int(result.group(1))
        from_location = int(result.group(2))
        to_location = int(result.group(3))

        for n in range(occurrences):
            box = stacks[from_location].pop()
            stacks[to_location].append(box)


if __name__ == '__main__':
    main()
