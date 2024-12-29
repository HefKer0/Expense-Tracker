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
    items = []  # Stores string indexes of values != spaces

    for index, current_value in enumerate(line):
        if current_value != " ":
            items.append(index)

    previous_value = None
    sequence = None
    previously = None

    string_starts = []
    string_ends = []

    for index, current_value in enumerate(items):
        if previous_value == current_value - 1:
            if sequence is not True:
                string_starts.append(current_value)
            sequence = True
        elif sequence is False and previously is True:  #
            print(f"No sequence and previously true at value: {current_value}")  #
        else:
            previously = sequence  #
            sequence = False
        previous_value = current_value


        string_ends.append(current_value)





def line_constructor():
    pass


def file_checker():
    # Check if file exists, if not then create one and append 1st line
    pass


line_parser("# 2   2024-08-06  Dinner       $10")