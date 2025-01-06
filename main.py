import argparse
import helper
from datetime import date


def line_parser(line: str):
    value_list = line.split()
    return value_list


def cmd_add(description, amount):
    last_line = helper.read_last_line(file)
    value_list = line_parser(last_line)
    last_id = int(value_list[1])
    helper.line_constructor(str(last_id + 1), str(date.today()), description, str(amount))


def cmd_list():
    with open(file, "r") as f:
        print(f.read())


def cmd_summary(month):
    if month:
        month_to_number = {
            "January": "01",
            "February": "02",
            "March": "03",
            "April": "04",
            "May": "05",
            "June": "06",
            "July": "07",
            "August": "08",
            "September": "09",
            "October": "10",
            "November": "11",
            "December": "12",
        }
        month_number = None
        try:
            int(month)
        except ValueError:
            """
            month == "january" month_number = ?
            get the month_number using "january"
            """
            month = month.capitalize()
            month_number = month_to_number.get(month, "Invalid month")
        else:
            """ 
            month = "1" or "01" month_number = 1 or 01
            if month == "1" add a 0 before
            get name of the month "January"
            """
            month_number_list = list(month)
            if len(month_number_list) < 2:
                month_number_list.append(0)
                month_number_list.reverse()
                month_number = "".join(map(str, month_number_list))
            else:
                month_number = month

            for k, v in month_to_number.items():
                if v == month_number:
                    month = k
                    break
        finally:
            expenses = 0.0

            with open(file, "r") as f:
                for x in f:
                    if "Date" in x:
                        pass
                    elif x[11:13] == month_number:
                        value_list = line_parser(x)
                        amount = float(value_list[4][1:-2])
                        expenses += amount

            print(f"Total expenses for {month}: ${expenses}")
    else:
        expenses = 0.0
        with open(file, "r") as f:
            for x in f:
                if "Date" in x:
                    pass
                else:
                    value_list = line_parser(x)
                    amount = float(value_list[4][1:-2])
                    expenses += amount
        print(f"Total expenses: ${expenses:.2f}")


def cmd_delete(expense_id):
    with open(file, "r") as f:
        lines = f.readlines()

    for index, line in enumerate(lines):
        if line[2:5].strip() == str(expense_id):
            del lines[index]
            break

    with open(file, "w") as f:
        for line in lines:
            f.write(line)

    print("Expense deleted successfully")


def main():
    helper.file_checker()

    parser = argparse.ArgumentParser(description="Track your expenses!")
    subparsers = parser.add_subparsers(dest="command", description="Available commands")

    # Add
    parser_add = subparsers.add_parser("add", help="Add a new expense")
    parser_add.add_argument("--description", "-d", required=True, type=str,
                            help="Description of the expense")
    parser_add.add_argument("--amount", "-a", required=True, type=float,
                            help="Amount of the expense")

    # List
    parser_list = subparsers.add_parser("list", help="List all expenses")

    # Summary
    parser_summary = subparsers.add_parser("summary", help="Show a summary of expenses")
    parser_summary.add_argument("--month", "-m", required=False, type=str,
                                help="Filter summary by month (e.g. '1' or 'January')")
    # Delete
    parser_delete = subparsers.add_parser("delete", help="Delete an expense by its id")
    parser_delete.add_argument("--id", "-id", type=int, help="id of the expense you want to delete")

    # Processing
    args = parser.parse_args()

    if args.command == "add":
        cmd_add(args.description, args.amount)
    elif args.command == "list":
        cmd_list()
    elif args.command == "summary":
        cmd_summary(args.month)
    elif args.command == "delete":
        cmd_delete(args.id)
    else:
        parser.print_help()


file = "database.txt"

if __name__ == "__main__":
    main()
