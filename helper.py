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
    start_index = 0
    index = start_index
    finished = False
    while not finished:
        while index < len(line_list):
            if line_list[index] == " " and line_list[index - 1] == ",":
                del line_list[index]
                break
            elif line_list[index] == " ":
                line_list[index] = ","
            index += 1
            if index == len(line_list):
                finished = True


def line_constructor():
    pass


def file_checker():
    # Check if file exists, if not then create one and append 1st line
    pass


line_parser("# 2   2024-08-06  Dinner       $10")
