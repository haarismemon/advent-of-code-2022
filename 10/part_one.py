import re


def main(file):
    with open(file) as input_file:
        preset_cycles = [20, 60, 100, 140, 180, 220]

        instructions = input_file.readlines()
        instruction_index = 0

        x = 1
        signal_strength = 0

        is_waiting_to_add = False
        stored_add_value = 0

        for cycle in range(1, max(preset_cycles) + 1):
            if cycle in preset_cycles:
                signal_strength += cycle * x
                print(f'preset cycle {cycle}: {cycle * x}')

            if is_waiting_to_add:
                x += int(stored_add_value)

                is_waiting_to_add = False
                stored_add_value = 0

                instruction_index += 1
                continue

            if instruction_index != len(instructions):
                instruction = instructions[instruction_index].rstrip('\n')
                add_pattern = "^addx (-?\\d+)$"

                if re.match(add_pattern, instruction):
                    add_value = re.search(add_pattern, instruction).group(1)

                    is_waiting_to_add = True
                    stored_add_value = add_value
                else:
                    instruction_index += 1

        print('final value', signal_strength)


if __name__ == '__main__':
    main('input.txt')
