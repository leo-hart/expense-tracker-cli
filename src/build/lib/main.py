import json
from datetime import datetime
import argparse
from pathlib import Path

DATA_FILE = Path('data/expenses.json')

def load_expenses():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
    
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

def add_expense(description, amount):
    if amount <= 0:
        print('Error: Amount should be positive')
        return
    
    expenses = load_expenses()
    new_id = max(expenses['id'] for expense in expenses) +1 if expenses else 1
    new_expense ={
        'id': new_id,
        'date': datetime.today().strftime('%Y-%m-%d'),
        'description': description,
        'amount': amount
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    print(f'Expense added succesfully - ID {new_id}')

def delete_expense(expense_id):
    expenses = load_expenses()
    for i, expense in enumerate(expenses):
        if expense['id'] == expense_id:
            del expenses[i]
            save_expenses(expenses)
            print(f'Expense deleted succesfully - ID {expense_id}')
            return
    print(f'Error: Item number {expense_id} does not exists')

def update_expense(expense_id, description=None, amount=None):
    expenses = load_expenses()
    for expense in expenses:
        if expense['id'] == expense_id:
            if description:
                expense['description'] = description
            if amount <= 0:
                print('Error: Amount must be positive')
                return
            expense['amount'] = amount
            save_expenses(expenses)
            print('Expense updated succesfully')

    print(f'Error: Expanse with ID {expense_id} not found')

def list_expenses():
    expenses=load_expenses()
    print('# ID    Date    Description    Amount')
    for expense in expenses:
        print(f'#{expense['id']: <2} {expense['date']} {expense['description']:<15} ${expense['amount']:.2f}')

def get_summary(month=None):
    expenses=load_expenses()
    current_year = datetime.now().year

    if month:
        if month <1 or month >12:
            print('Error: Month should be between 1 and 12')
            return
        
        filtered = [
            e for e in expenses
            if datetime.strptime(e['date'], '%Y-%m-%d').month == month
            and datetime.strptime(e['date'], '%Y-%m-%d').year == current_year
        ]
        total = sum(e['amount'] for e in filtered)
        month_name = datetime(current_year, month, 1).strftime('%B')
        print(f'# Total expenses for {month_name}: ${total:.2f}')
    else:
        total = sum(e['amount'] for e in expenses)
        print(f'# Total expenses: ${total:.2f}')


def main():
    parser = argparse.ArgumentParser(prog='tracker')
    subparsers = parser.add_subparsers(dest='command')

    #add
    add_parser=subparsers.add_parser('add')
    add_parser.add_argument('--description', required=True)
    add_parser.add_argument('--amount', type=float, required=True)

    #delete
    delete_parser=subparsers.add_parser('delete')
    delete_parser.add_argument("--id", type=int, required=True)
    
    #update
    update_parser=subparsers.add_parser('update')
    update_parser.add_argument('--id', type=int, required=True)
    update_parser.add_argument('--description')
    update_parser.add_argument('--amount', type=float)
                                    
    #list
    subparsers.add_parser('list')

    #summary
    summary_parser=subparsers.add_parser('summary')                               
    summary_parser.add_argument('--month', type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        get_summary(args.month)    
    else:
        print(parser.print_help)

if __name__ == "__main__":
    main()