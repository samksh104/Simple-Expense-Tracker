import os

FILE_NAME = "expenses.txt"

def add_expense(amount, category, note=""):
    with open(FILE_NAME, "a") as file:
        file.write(f"{amount},{category},{note}\n")
    print(f"✅ Added ₹{amount} to {category}.")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("📭 No expenses recorded.")
        return
    with open(FILE_NAME, "r") as file:
        print("\n📋 Your Expenses:")
        total = 0
        for line in file:
            parts = line.strip().split(",")
            amount = float(parts[0])
            category = parts[1]
            note = parts[2] if len(parts) > 2 else ""
            print(f"₹{amount} | Category: {category} | Note: {note}")
            total += amount
        print(f"\n💰 Total Spent: ₹{total}")

def main():
    print("💸 Simple Expense Tracker")
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Choose (1/2/3): ")
        if choice == "1":
            try:
                amount = float(input("Enter amount (₹): "))
                category = input("Enter category (e.g., Food, Travel): ")
                note = input("Optional note: ")
                add_expense(amount, category, note)
            except ValueError:
                print("⚠️ Please enter a valid amount.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("👋 Exiting... Stay on budget!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
