def read_last_line(filename):
    with open(filename, "rb") as file:
        file.seek(-2, 2)
        while file.read(1) != b"\n":
            file.seek(-2, 1)
        last_line = file.readline().decode()
    return last_line.strip()


def line_parser(filename, line, mode):
    pass


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