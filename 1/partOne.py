def main():
    with open('dummy.txt') as input_file:
        max_calories_of_elves = 0
        current_elf_sum = 0

        for line in input_file:
            calorie = line.rstrip('\n')

            if calorie == '':
                if current_elf_sum > max_calories_of_elves:
                    max_calories_of_elves = current_elf_sum
                current_elf_sum = 0
            else:
                current_elf_sum += int(calorie)

        if current_elf_sum != 0:
            if current_elf_sum > max_calories_of_elves:
                max_calories_of_elves = current_elf_sum

        print(max_calories_of_elves)

if __name__ == '__main__':
    main()
