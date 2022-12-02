def my_move_points(my_move):
    points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    return points[my_move]


def main():
    with open('input.txt') as input_file:
        total_score = 0

        for line in input_file:
            game_round = line.rstrip('\n').split(' ')

            elf_play = game_round[0]
            my_play = game_round[1]

            score = 0

            if elf_play == 'A':
                if my_play == 'X':
                    score = my_move_points('X') + 3
                elif my_play == 'Y':
                    score = my_move_points('Y') + 6
                elif my_play == 'Z':
                    score = my_move_points('Z') + 0
                else:
                    score = 0
            elif elf_play == 'B':
                if my_play == 'X':
                    score = my_move_points('X') + 0
                elif my_play == 'Y':
                    score = my_move_points('Y') + 3
                elif my_play == 'Z':
                    score = my_move_points('Z') + 6
                else:
                    score = 0
            elif elf_play == 'C':
                if my_play == 'X':
                    score = my_move_points('X') + 6
                elif my_play == 'Y':
                    score = my_move_points('Y') + 0
                elif my_play == 'Z':
                    score = my_move_points('Z') + 3
                else:
                    score = 0
            else:
                score = 0

            total_score += score
            print(elf_play, my_play, '=', score)

        print(total_score)


if __name__ == '__main__':
    main()
