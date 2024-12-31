# I literally spent hours on this
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

    # Return id
    start_index = 2
    index = start_index
    finished = False
    expense_id = []
    while not finished:
        if line_list[index] == ",":
            finished = True
        else:
            expense_id.append(line_list[index])
        index += 1

    return int("".join(expense_id))

# And then I realized split() does the same but better

def line_parser(line: str):
    value_list = line.split()
    return value_list