def main():
    with open('input.txt') as input_file:
        line = input_file.readline().rstrip('\n')

        char_progress = ""
        last_four_characters = ""
        start_index = 0
        last_occurrence_of_char = {}

        for i in range(len(line)):
            c = line[i]

            if c in last_four_characters:
                start_index = last_occurrence_of_char[c] + 1

            last_occurrence_of_char[c] = i
            char_progress += c

            last_four_characters = char_progress[start_index:]

            if len(last_four_characters) == 4:
                print('first marker:', c, i + 1)
                break


if __name__ == '__main__':
    main()