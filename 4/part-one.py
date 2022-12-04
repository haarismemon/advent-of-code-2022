
def main():
    with open('input.txt') as input_file:
        full_contained_count = 0

        for line in input_file:
            stripped_line = line.rstrip('\n')

            pairs = stripped_line.split(',')
            first_section = [int(n) for n in pairs[0].split('-')]
            second_section = [int(n) for n in pairs[1].split('-')]

            if first_section[0] > second_section[0]:
                if first_section[1] <= second_section[1]:
                    full_contained_count += 1
            elif first_section[0] == second_section[0]:
                full_contained_count += 1
            else:
                if second_section[1] <= first_section[1]:
                    full_contained_count += 1

        print('fully contained count:', full_contained_count)


if __name__ == '__main__':
    main()
