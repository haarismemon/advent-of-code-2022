def my_move_points(my_move):
    points = {
        "R": 1,
        "P": 2,
        "S": 3
    }
    return points[my_move]


def main():
    with open('input.txt') as input_file:
        total_score = 0

        for line in input_file:
            game_round = line.rstrip('\n').split(' ')

            elf_play = game_round[0]
            my_outcome = game_round[1]

            score = 0

            # rock
            if elf_play == 'A':
                if my_outcome == 'X':
                    score = my_move_points('S') + 0
                elif my_outcome == 'Y':
                    score = my_move_points('R') + 3
                elif my_outcome == 'Z':
                    score = my_move_points('P') + 6
                else:
                    score = 0
            # paper
            elif elf_play == 'B':
                if my_outcome == 'X':
                    score = my_move_points('R') + 0
                elif my_outcome == 'Y':
                    score = my_move_points('P') + 3
                elif my_outcome == 'Z':
                    score = my_move_points('S') + 6
                else:
                    score = 0
            # scissors
            elif elf_play == 'C':
                if my_outcome == 'X':
                    score = my_move_points('P') + 0
                elif my_outcome == 'Y':
                    score = my_move_points('S') + 3
                elif my_outcome == 'Z':
                    score = my_move_points('R') + 6
                else:
                    score = 0
            else:
                score = 0

            total_score += score
            print(elf_play, my_outcome, '=', score)

        print(total_score)


if __name__ == '__main__':
    main()
