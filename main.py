import csv
import os

FILE = "expenses.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Amount"])


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, amount])

    print("Expense added!\n")


def view_expenses():
    print("\nExpenses:\n")
    total = 0

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            print(row)
            total += float(row[1])

    print("\nTotal Spending:", total)


def delete_last():
    with open(FILE, "r") as f:
        rows = list(csv.reader(f))

    if len(rows) > 1:
        removed = rows.pop()

        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print("Deleted:", removed)
    else:
        print("No data to delete")


while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Last Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_last()
    elif choice == "4":
        break
    else:
        print("Invalid choice")