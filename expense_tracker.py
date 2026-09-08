
from datetime import date
import pymysql


# Database Connection
def connect_database():
    try:
        return pymysql.connect(
            host="localhost",
            user="root",
            password="YOUR_MYSQL_PASSWORD",
            database="expense_tracker"
        )
    except Exception as e:
        print("Database Error:", e)
        return None


# 1. Add Expense
def add_expense():
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return

    description = input("Enter description: ")

    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses(expense_date, category, description, amount) "
        "VALUES(%s, %s, %s, %s)",
        (date.today(), category, description, amount)
    )

    conn.commit()

    print("Expense added successfully!")

    conn.close()


# 2. View Expenses
def view_expenses():
    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses ORDER BY expense_id")

    records = cursor.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print("No expenses found.")

    conn.close()


# 3. Update Expense
def update_expense():
    try:
        expense_id = int(input("Enter expense ID: "))
        amount = float(input("Enter new amount: "))
    except ValueError:
        print("Invalid input!")
        return

    category = input("Enter new category: ")
    description = input("Enter new description: ")

    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute(
        "UPDATE expenses SET category=%s, amount=%s, description=%s "
        "WHERE expense_id=%s",
        (category, amount, description, expense_id)
    )

    conn.commit()

    if cursor.rowcount:
        print("Expense updated!")
    else:
        print("Expense not found.")

    conn.close()


# 4. Delete Expense
def delete_expense():
    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE expense_id=%s",
        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount:
        print("Expense deleted!")
    else:
        print("Expense not found.")

    conn.close()


# 5. Total Expense
def total_expense():
    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0] or 0

    print(f"Total Expense: ₹{total:.2f}")

    conn.close()


# 6. Search Expense
def search_expense():
    category = input("Enter category to search: ")

    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE category LIKE %s",
        ("%" + category + "%",)
    )

    records = cursor.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print("No expenses found.")

    conn.close()


# 7. Category-wise Expense
def category_expense():
    conn = connect_database()

    if conn is None:
        return

    cursor = conn.cursor()

    cursor.execute(
        "SELECT category, SUM(amount) "
        "FROM expenses GROUP BY category"
    )

    records = cursor.fetchall()

    if records:
        for row in records:
            print(row)
    else:
        print("No expenses found.")

    conn.close()


# Main Menu
def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Total Expense")
        print("6. Search Expense")
        print("7. Category-wise Expense")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            update_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            total_expense()

        elif choice == "6":
            search_expense()

        elif choice == "7":
            category_expense()

        elif choice == "8":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
