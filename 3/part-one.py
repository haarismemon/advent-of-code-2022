import string


def main():
    alphabets = list(string.ascii_lowercase + string.ascii_uppercase)
    numbers = range(1, 53)

    priorities = dict(zip(alphabets, numbers))

    with open('input.txt') as input_file:
        total_priority = 0

        for line in input_file:
            rucksack = line.rstrip('\n')
            half_length = int(len(rucksack)/2)

            first_rucksack = rucksack[:half_length]
            second_rucksack = rucksack[half_length:]

            common_char = ""

            for c in first_rucksack:
                if c in second_rucksack:
                    common_char = c
                    break

            total_priority += priorities[common_char]
            print(rucksack, 'common character: ', common_char)

        print('total priority = ', total_priority)


if __name__ == '__main__':
    main()
