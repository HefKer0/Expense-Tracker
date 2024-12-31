import argparse
import helper
from datetime import date


def cmd_add(description, amount):
    last_line = helper.read_last_line(file)
    last_id = helper.line_parser(last_line)
    helper.line_constructor(str(last_id + 1), str(date.today()), description, str(amount))


def cmd_list():
    print("list")
    pass


def cmd_summary(month):
    if month is True:
        print(month)
    else:
        print("Summary")
    pass


def cmd_delete(expense_id):
    print(expense_id)
    pass


def main():
    helper.file_checker()

    parser = argparse.ArgumentParser(description="Track your expenses!")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add
    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument("--description", required=True, type=str, help="Description of the expense")  # L
    add_parser.add_argument("--amount", required=True, type=float, help="Amount of the expense")

    # List
    list_parser = subparsers.add_parser("list", help="List all expenses")

    # Summary
    summary_parser = subparsers.add_parser("summary", help="Show a summary of expenses")
    summary_parser.add_argument("--month", required=False, type=str,
                                help="Filter summary by month (e.g. '1' or 'January')")

    # Delete
    delete_parser = subparsers.add_parser("delete", help="Delete an expense using its id")
    delete_parser.add_argument("id", type=int, help="id of the expense you want to delete")

    # Parse
    args = parser.parse_args()

    # Route
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
