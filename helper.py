import re


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


def line_parser(line, mode):
    expense_id = 0
    expense_date = ""
    expense_description = ""
    expense_amount = 0

    spaces = find_character_positions(line, " ")
    items = []

    # Detect sequence
    previous_char = None

    for index, current_char in enumerate(spaces):
        if previous_char == current_char:

        previous_char = current_char


def line_constructor():
    pass


def file_checker():
    # Check if file exists, if not then create one and append 1st line
    pass


expense = {
    "ID": 2,
    "Date": "2024-08-06",
    "Description": "Dinner",
    "Amount": "$10"
}
print(expense["ID"])

expense_id = 2

expense = {
    "ID": expense_id,
    "Date": expense_date,
    "Description": expense_description,
    "Amount": expense_amount
}
# ID  Date       Description  Amount
# 2   2024-08-06  Dinner       $10

"""
by pos (begins at)
#:
ID:
Date:
Desc:
Amount:
"""


