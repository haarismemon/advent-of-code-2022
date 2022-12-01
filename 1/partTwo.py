def main():
    with open('input.txt') as input_file:
        list_of_sum_calories = []
        current_elf_sum = 0

        for line in input_file:
            calorie = line.rstrip('\n')

            if calorie == '':
                list_of_sum_calories.append(current_elf_sum)
                current_elf_sum = 0
            else:
                current_elf_sum += int(calorie)

        if current_elf_sum != 0:
            list_of_sum_calories.append(current_elf_sum)

        list_of_sum_calories.sort(reverse=True)

        print(list_of_sum_calories)
        print(sum(list_of_sum_calories[0:3]))


if __name__ == '__main__':
    main()
