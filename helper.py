from operator import invert


def find_character_positions(input_string: str, target_characters: str):
    positions = [index for index, char in enumerate(input_string) if char in target_characters]
    return positions


def read_last_line(filename: str):
    with open(filename, "rb") as file:
        file.seek(-2, 2)
        while file.read(1) != b"\n":
            file.seek(-2, 1)
        last_line = file.readline().decode()
    return last_line.strip()


def line_parser(line):
    line_list = list(line)
    del_list = []
    change = None
    # Run until no changes are made?

    for index, value in enumerate(line_list):
        if value == " " and line_list[index - 1] == ",":
            del_list.append(index)
        elif value == " ":
            line_list[index] = ","

    for x in reversed(del_list):
        del line_list[x]

    for x in


def line_constructor():
    pass


def file_checker():
    # Check if file exists, if not then create one and append 1st line
    pass


line_parser("# 2   2024-08-06  Dinner       $10")
