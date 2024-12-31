import os

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


def line_constructor(e_id: str, date: str, description: str, amount: str):
    line = ['#', ' ']
    def appender(iterable):
        for z in iterable:
            line.append(z)

    def length_extender(length: int):
        while len(line) < length:
            line.append(" ")

    appender(e_id)
    length_extender(6)
    appender(date)
    length_extender(18) #
    appender(description)
    length_extender(31)
    line.append("$")
    appender(amount)

    with open("database.txt", "a") as f:
        f.write("\n")
        for x in line:
            f.write(x)


def file_checker():
    # Check if file exists, if not then create one and append 1st line
    if os.path.exists("database.txt"):
        pass
    else:
        with open("database.txt", "a") as f:
            f.write("# ID  Date       Description  Amount")