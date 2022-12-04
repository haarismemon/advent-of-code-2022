
def main():
    with open('input.txt') as input_file:
        partially_contained_count = 0

        for line in input_file:
            stripped_line = line.rstrip('\n')

            pairs = stripped_line.split(',')
            first_section = [int(n) for n in pairs[0].split('-')]
            second_section = [int(n) for n in pairs[1].split('-')]

            if first_section[0] > second_section[0]:
                if second_section[1] >= first_section[0]:
                    partially_contained_count += 1
            elif first_section[0] == second_section[0]:
                partially_contained_count += 1
            else:
                if first_section[1] >= second_section[0]:
                    partially_contained_count += 1

        print('partially contained count:', partially_contained_count)


if __name__ == '__main__':
    main()
