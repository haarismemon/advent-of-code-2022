def main(num_distinct_chars):
    with open('input.txt') as input_file:
        input = input_file.readline().rstrip('\n')

        distinct_chars = ""
        start_index = 0
        last_occurrence_of_char = {}

        for i in range(len(input)):
            c = input[i]

            if c in distinct_chars:
                start_index = last_occurrence_of_char[c] + 1

            last_occurrence_of_char[c] = i
            distinct_chars = input[start_index:i+1]

            if len(distinct_chars) == num_distinct_chars:
                return i + 1


if __name__ == '__main__':
    print('part one, first marker:', main(4))
    print('part two, first marker:', main(14))
