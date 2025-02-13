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
    git clone https://github.com/your-username/expense-tracker-cli.git
    cd expense-tracker-cli
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
![Image](https://github.com/user-attachments/assets/a907f993-a737-49f5-ba5e-adf6d98f399b)

2. List
    ```bash
    # List all the expenses
    tracker list
![Image](https://github.com/user-attachments/assets/5465294d-0735-4564-87a4-a49320aee1d1)

3. Delete
    ```bash
    # Users can delete an expense based on its id.
    tracker delete --id 4
![Image](https://github.com/user-attachments/assets/f569d3ff-677e-4616-bd4a-74e337bb1d64)

4. Update
    ```bash
    # Users can update an expense.
    tracker update --id 4 --amount 32
![Image](https://github.com/user-attachments/assets/aa94e9d9-68e3-4fe4-9bb1-dcfefe534d5f)

5. Summary
    ```bash
    # Users can view a sum of all expenses.
    tracker summary

    # Users can view a sum of expenses for a specific month.
    tracker summary --month 1    
![Image](https://github.com/user-attachments/assets/108de844-ec2b-49be-8343-00085b474f58)

6. Export
    ```bash
    # Users can export expenses to a CSV file.
    tracker export --output expenses.csv
![Image](https://github.com/user-attachments/assets/0967a2fc-2bf5-470d-a312-221b63d18cac)

## Technologies Used
-    Python: The core programming language used for development.
-    argparse: For parsing command-line arguments and creating a user-friendly CLI.
-    pathlib: For handling file paths in a cross-platform manner.
-    JSON: For storing and managing expense data.
