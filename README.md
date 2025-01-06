# Expense Tracker

 - https://roadmap.sh/projects/expense-tracker

This is my first Python learning project, an expense management application built per these [requirements (roadmap.sh)](https://roadmap.sh/projects/expense-tracker)

# Running

1. Download main.py and helpers.py and put them in the same folder
2. CLI: `python main.py -h`

- A database.txt file will be created when first running the `add` command

# Uses

1. Adding a new expense with `add`
	- `py main.py add --description Food --amount 20`
	- `py main.py add -d Food -a 20`
2. List all expenses with `list`
	- `py main.py list`
	- `py main.py list --month 1` 
		
3. Show a summary of expenses with `summary`
	- `py main.py summary --month 1`
		-  `--month` or `-m`
		- Supports `01`, `1`, `JaNuARY`
4. Delete an expense by its ID with `delete`
	- `py main.py delete 1`

# Issues

There are a few issues I’m too lazy to fix
1. Description with a length of 13 or more breaks the program [Issue#6](https://github.com/HefKer0/Expense-Tracker/issues/6)
2. `summary` will show expenses for previous years
3. `add` does not give feedback after adding an expense
