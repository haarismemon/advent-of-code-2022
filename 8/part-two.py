def main(file):
    with open(file) as input_file:
        matrix = []

        for line in input_file:
            row = line.rstrip('\n')
            number_row = [int(x) for x in row]
            matrix.append(number_row)

        height = len(matrix)
        width = len(matrix[0])

        scenic_scores = []

        for y in range(height):
            for x in range(width):
                scenic_scores.append(scenic_score(matrix, x, y))

        print('highest scenic score is:', max(scenic_scores))


def scenic_score(matrix, x, y):
    tree = matrix[y][x]

    # sort adjacent trees from the current tree outwards
    left_trees = matrix[y][:x]
    left_trees.reverse()
    right_trees = matrix[y][x+1:]
    up_trees = list(map(lambda row: row[x], matrix[:y]))
    up_trees.reverse()
    down_trees = list(map(lambda row: row[x], matrix[y+1:]))

    surrounding_trees = [left_trees, right_trees, up_trees, down_trees]

    scenic_score_num = None
    for tree_list in surrounding_trees:
        count = 0

        for t in tree_list:
            count += 1
            if t >= tree:
                break

        if scenic_score_num is None:
            scenic_score_num = count
        else:
            scenic_score_num *= count

    return scenic_score_num


if __name__ == '__main__':
    main('input.txt')
