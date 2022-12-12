import re
import numpy


class Monkey:
    items = []
    operation: (str, str) = None
    test: int = 1
    true_monkey: int = 0
    false_monkey: int = 0
    total_items_inspected = 0

    def __init__(self, number):
        self.number = number


def parse_monkey_instructions():
    current_monkey = None

    re_monkey_num = "^Monkey (\\d+):\\n$"
    re_starting_items = ".*items: (.+)\\n$"
    re_operation = ".*old.*([\\*\\+]) (.*)$"
    re_test = ".*divisible by (\\d+)\\n$"
    re_true_monkey = ".*true.*monkey (\\d+)\\n$"
    re_false_monkey = ".*false.*monkey (\\d+)\\n$"

    for input_line in input_array:
        if input_line == "\n":
            continue
        if re.match(re_monkey_num, input_line):
            monkey_num: int = int(re.search(re_monkey_num, input_line).group(1))
            current_monkey = Monkey(monkey_num)
            monkeys[monkey_num] = current_monkey
        elif re.match(re_starting_items, input_line):
            starting_items = re.search(re_starting_items, input_line).group(1).split(", ")
            current_monkey.items = [int(x) for x in starting_items]
        elif re.match(re_operation, input_line):
            operation_match = re.search(re_operation, input_line)
            current_monkey.operation = operation_match.group(1), operation_match.group(2)
        elif re.match(re_test, input_line):
            test_division = re.search(re_test, input_line).group(1)
            current_monkey.test = int(test_division)
        elif re.match(re_true_monkey, input_line):
            true_monkey = re.search(re_true_monkey, input_line).group(1)
            current_monkey.true_monkey = int(true_monkey)
        elif re.match(re_false_monkey, input_line):
            false_monkey = re.search(re_false_monkey, input_line).group(1)
            current_monkey.false_monkey = int(false_monkey)


def perform_operation(operation: (str, str), old_value: int):
    op = operation[0]
    value_string = operation[1]

    if value_string == "old":
        value = old_value
    else:
        value = int(value_string)

    if op == "+":
        return old_value + value
    elif op == "*":
        return old_value * value
    else:
        return old_value


def perform_round():
    for monkey in monkeys.values():
        for item in monkey.items:
            new_value = perform_operation(monkey.operation, item)
            item_worry_level = new_value // 3
            test = item_worry_level % monkey.test == 0

            if test:
                monkeys[monkey.true_monkey].items.append(item_worry_level)
            else:
                monkeys[monkey.false_monkey].items.append(item_worry_level)

            monkey.total_items_inspected += 1

        monkey.items = []


file_name = 'input.txt'
with open(file_name) as input_file:
    total_rounds = 20

    input_array = input_file.readlines()
    monkeys = {}

    parse_monkey_instructions()

    for i in range(total_rounds):
        perform_round()

    total_inspected_list = list(map(lambda m: m.total_items_inspected, monkeys.values()))
    total_inspected_list.sort(reverse=True)
    monkey_business = numpy.prod(total_inspected_list[:2])

    print(f'monkey business: {monkey_business}')
