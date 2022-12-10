import re


def main(file):
    with open(file) as input_file:
        preset_cycles = [40, 80, 120, 160, 200, 240]

        instructions = input_file.readlines()
        instruction_index = 0

        x = 1

        is_waiting_to_add = False
        stored_add_value = 0

        whole_crt = ""
        current_crt_row = ""
        current_crt_index = 0

        for cycle in range(1, max(preset_cycles) + 1):
            if current_crt_index in range(x - 1, x + 2):
                current_crt_row = current_crt_row + "#"
            else:
                current_crt_row = current_crt_row + "."
            current_crt_index += 1

            if cycle in preset_cycles:
                whole_crt = whole_crt + "\n" + current_crt_row
                current_crt_index = 0
                current_crt_row = ""

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

        print(whole_crt)


if __name__ == '__main__':
    main('input.txt')
