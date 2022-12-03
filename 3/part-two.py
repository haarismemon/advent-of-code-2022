import string


def main():
    alphabets = list(string.ascii_lowercase + string.ascii_uppercase)
    numbers = range(1, 53)

    priorities = dict(zip(alphabets, numbers))

    with open('input.txt') as input_file:
        total_priority = 0
        group_of_three = []

        for line in input_file:
            rucksack = line.rstrip('\n')
            common_char = ''

            group_of_three.append(rucksack)

            if len(group_of_three) == 3:
                group_of_three.sort(key=len, reverse=True)
                largest_rucksack = group_of_three[0]

                for c in largest_rucksack:
                    if c in group_of_three[1] and c in group_of_three[2]:
                        common_char = c
                        break

                if common_char != '':
                    group_of_three = []
                    total_priority += priorities[common_char]
                    print('common character: ', common_char)

        print('total priority = ', total_priority)


if __name__ == '__main__':
    main()
