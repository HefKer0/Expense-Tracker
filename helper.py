import os
from datetime import date

def read_last_line(filename: str):
    with open(filename, "rb") as file:
        file.seek(-2, 2)
        while file.read(1) != b"\n":
            file.seek(-2, 1)
        last_line = file.readline().decode()
    return last_line.strip()


def line_constructor(e_id: str, e_date: str, description: str, amount: str):
    line = ['#', ' ']
    def appender(iterable):
        for z in iterable:
            line.append(z)

    def length_extender(length: int):
        while len(line) < length:
            line.append(" ")

    appender(e_id)
    length_extender(6)
    appender(e_date)
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