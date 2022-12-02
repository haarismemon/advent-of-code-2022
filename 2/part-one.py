points = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
mappings = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}
to_win = {
    "A": "B",
    "B": "C",
    "C": "A"
}


def main():
    with open('input.txt') as input_file:
        total_score = 0

        for line in input_file:
            game_round = line.rstrip('\n').split(' ')

            elf_play = game_round[0]
            my_play = game_round[1]

            score = points[my_play]

            # draw
            if elf_play == mappings[my_play]:
                score += 3
            # win
            elif (elf_play, mappings[my_play]) in to_win.items():
                score += 6

            total_score += score
            print(elf_play, my_play, '=', score)

        print(total_score)


if __name__ == '__main__':
    main()
