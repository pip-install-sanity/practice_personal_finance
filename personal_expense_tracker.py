import pandas as pd
import matplotlib.pyplot as plt

# --- Step 1: Create a CSV file with sample data ---
data = {
    'Date': ['2025-04-01', '2025-04-01', '2025-04-02','2025-04-02', '2025-04-03'],
    'Category': ['Food', 'Transportation', 'Bills', 'Food', 'Food'],
    'Amount': [250, 100, 300, 200, 150],
}

with open('expenses.csv', 'w') as file:
    file.write('Date,Category,Amount\n') 

    for i in range(len(data['Date'])):
        file.write(f"{data['Date'][i]},{data['Category'][i]},{data['Amount'][i]}\n") # [i] signifies

# --- Step 2: Read the CSV file into a DataFrame ---
df = pd.read_csv('expenses.csv')

# --- Step 3: Add a new expense if the user has one ---

update = input("Do you have a new update? (yes/no): ").strip().lower()

if update not in ['yes', 'no']:
    print("Invalid input. Please enter 'yes' or 'no'.")
    exit()

if update == 'yes':
    try:
        new_expense = input("Enter new expense (Date, Category, Amount): ").split(",")
        if len(new_expense) != 3:
            raise ValueError("Please enter exactly 3 values separated by commas.")
        new_expense[2] = int(new_expense[2].strip())
    except ValueError as e:
        print(f"Error: {e} Please enter the data in the correct format.")
        exit()
else:
    new_expense = None #

if new_expense:
    new_row = {
        'Date': new_expense[0].strip(),
        'Category': new_expense[1].strip(),
        'Amount': int(new_expense[2].strip())
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv('expenses.csv', index=False)

# --- Step 4: Analyze the data ---
total = df['Amount'].sum()
per_category = df.groupby('Category')['Amount'].sum()
highest_day = df.groupby('Date')['Amount'].sum().idxmax()

print(f"Total Expenses: ₱{total}")
print("\nSpending per Category:")
print(per_category)
print(f"\nDay with Highest spending: {highest_day}")

# --- Step 5: Visualize the data ---
plt.figure(figsize=(10, 6))
plt.bar(per_category.index, per_category.values, color='blue')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.title('Expenses by Category')

plt.show()