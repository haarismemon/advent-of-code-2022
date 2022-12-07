import part_one


def main(file):
    with open(file) as input_file:
        all_directories = []
        root_directory = part_one.Directory(None)

        part_one.read_commands(input_file, root_directory, all_directories)
        part_one.calculate_directory_sizes(all_directories)

        directory_sizes = sorted(list(map(lambda directory: directory.contents_size, all_directories)))
        print(f'Size of directory to delete:', clear_up_space(directory_sizes, root_directory))


def clear_up_space(directory_sizes, root_directory: part_one.Directory):
    total_storage = 70000000
    minimum_unused_space = 30000000
    current_unused = total_storage - root_directory.contents_size
    space_needed = minimum_unused_space - current_unused

    if space_needed > 0:
        filtered_directories = list(filter(lambda directory: directory >= space_needed, directory_sizes))
        return filtered_directories[0]
    else:
        return None


if __name__ == '__main__':
    main('input.txt')
