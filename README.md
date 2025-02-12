# Expense Tracker

A command-line expense tracker application to manage personal finances.

## Features
- Add, delete, update, and list expenses.
- View a summary of total expenseses; View a summary for a specific month.
- Export expenses to a CSV file.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/leo-hart/expense-tracker-cli.git

2. Navigate to project folder:
   ```bash
   cd expense-tracker-cli

3. Set up a virtual environment
    ```bash
    python -m venv venv

4. Activate
    ```bash
    On Windows:
    .\venv\Scripts\Acti vate

    On macOS/Linux:
    source venv/bin/activate

5. Instal dependencies
    ```bash
    pip install -e .

## Usage
1. Add
    ```bash
    # Users can add an expense with a description and amount.
    tracker add --description "Lunch" --amount 16
![Demo](assets\add.gif)

2. List
    ```bash
    # List all the expenses
    tracker list
![Demo](assets\list.gif)

3. Delete
    ```bash
    # Users can delete an expense based on its id.
    tracker delete --id 4
![Demo](assets\delete.gif)

4. Update
    ```bash
    # Users can update an expense.
    tracker update --id 4 --amount 32
![Demo](assets\update.gif)

5. Summary
    ```bash
    # Users can view a sum of all expenses.
    tracker summary

    # Users can view a sum of expenses for a specific month.
    tracker summary --month 1    
![Demo](assets\summary.gif)

6. Export
    ```bash
    # Users can export expenses to a CSV file.
    tracker export --output expenses.csv
![Demo](assets\export.gif)
