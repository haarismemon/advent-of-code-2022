points = {
    "A": 1,
    "B": 2,
    "C": 3
}
to_win = {
    "A": "B",
    "B": "C",
    "C": "A"
}
to_lose = {
    "A": "C",
    "B": "A",
    "C": "B"
}


def main():
    with open('input.txt') as input_file:
        total_score = 0

        for line in input_file:
            game_round = line.rstrip('\n').split(' ')

            elf_play = game_round[0]
            my_outcome = game_round[1]

            score = 0

            # draw
            if my_outcome == 'Y':
                score += points[elf_play] + 3
            # win
            elif my_outcome == "Z":
                my_move = to_win[elf_play]
                score += points[my_move] + 6
            # lose
            elif my_outcome == "X":
                my_move = to_lose[elf_play]
                score += points[my_move]

            total_score += score
            print(elf_play, my_outcome, '=', score)

        print(total_score)


if __name__ == '__main__':
    main()
