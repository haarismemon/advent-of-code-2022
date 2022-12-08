def main(file):
    with open(file) as input_file:
        matrix = []

        for line in input_file:
            row = line.rstrip('\n')
            number_row = [int(x) for x in row]
            matrix.append(number_row)

        height = len(matrix)
        width = len(matrix[0])

        seen_count = 0

        for y in range(height):
            row = ""
            for x in range(width):
                if can_be_seen(matrix, x, y):
                    seen_count += 1
                    row += "y"
                else:
                    row += "n"

        print('total trees that can be seen:', seen_count)


def is_on_edge(matrix, x, y) -> bool:
    if x == 0 or y == 0:
        return True
    if x == len(matrix[0]) - 1 or y == len(matrix) - 1:
        return True

    return False


def can_be_seen(matrix, x, y) -> bool:
    if is_on_edge(matrix, x, y):
        return True

    tree = matrix[y][x]

    # sort adjacent trees from the current tree inwards
    left_trees = matrix[y][:x]
    right_trees = matrix[y][x+1:]
    right_trees.reverse()
    up_trees = list(map(lambda row: row[x], matrix[:y]))
    down_trees = list(map(lambda row: row[x], matrix[y+1:]))
    down_trees.reverse()

    surrounding_trees = [left_trees, right_trees, up_trees, down_trees]

    is_all_small = False

    for tree_list in surrounding_trees:
        for t in tree_list:
            if t < tree:
                is_all_small = True
            else:
                is_all_small = False
                break

        if is_all_small:
            break

    return is_all_small


if __name__ == '__main__':
    main('input.txt')
