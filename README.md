# Expense Tracker

A command-line application to manage personal finances with ease.

The Expense Tracker is a powerful yet simple command-line tool designed to help you manage your expenses efficiently. Whether you're tracking daily spending, monitoring monthly budgets, or exporting financial data for analysis, this application has you covered. 

## Features
- Add Expenses: Quickly log expenses with a description and amount.
- Delete Expenses: Remove unwanted or incorrect entries.
- Update Expenses: Modify existing expense details.
- List Expenses: View all expenses in a clean, tabular format.
- Expense Summary: Get a total summary of expenses or filter by month.
- Export to CSV: Export your expense data to a CSV file for further analysis or sharing.
- Cross-Platform: Works seamlessly on Windows, macOS, and Linux.

## Installation
1. Installation:
    ```bash
    git clone https://github.com/your-username/expense-tracker.git
    cd expense-tracker
    python -m venv venv

    # On macOS
    source venv/bin/activate  
    # On Windows: 
    .\venv\Scripts\Activate

    pip install -e .

## How To Use
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

## Technologies Used
-    Python: The core programming language used for development.
-    argparse: For parsing command-line arguments and creating a user-friendly CLI.
-    pathlib: For handling file paths in a cross-platform manner.
-    JSON: For storing and managing expense data.