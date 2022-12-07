import re


class Directory:
    contents_size = 0

    def __init__(self, parent):
        self.parent_directory = parent
        self.child_directories = {}

    def add_new_file(self, file_size):
        self.contents_size += file_size

        if self.parent_directory:
            self.parent_directory.add_new_file(file_size)


def main(file):
    with open(file) as input_file:
        all_directories = []
        root_directory = Directory(None)

        read_commands(input_file, root_directory, all_directories)

        threshold = 100000

        result = sum(map(lambda d: d.contents_size if d.contents_size < threshold else 0, all_directories))

        print(f'Sum of directories above {threshold}: {result}')


def read_commands(input_file, root_directory, all_directories):
    current_directory = None
    printing_contents = False

    for line in input_file:
        command = line.rstrip('\n')
        cd_pattern = "^\\$ cd (.*)$"

        if re.match(cd_pattern, command):
            printing_contents = False
            result = re.search(cd_pattern, command)

            directory_name = result.group(1)

            if directory_name == '/':
                current_directory = root_directory
                all_directories.append(current_directory)
            elif directory_name == '..':
                current_directory = current_directory.parent_directory
            else:
                if directory_name in current_directory.child_directories:
                    current_directory = current_directory.child_directories[directory_name]
                    all_directories.append(current_directory)

        elif '$ ls' in command:
            printing_contents = True

        elif printing_contents:
            dir_pattern = "^dir (.*)$"
            file_pattern = "^(\\d+) (.*)$"

            if re.match(dir_pattern, command):
                directory_name = re.search(dir_pattern, command).group(1)
                new_directory = Directory(current_directory)
                current_directory.child_directories[directory_name] = new_directory
            elif re.match(file_pattern, command):
                file_size = int(re.search(file_pattern, command).group(1))
                current_directory.add_new_file(file_size)


if __name__ == '__main__':
    main('input.txt')
