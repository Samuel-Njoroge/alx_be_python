# Income and Expenses
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

# Montly savings 
monthly_savings = monthly_income - monthly_expenses
print(f"Your monthly savings are {monthly_savings}.")

# Projected annual savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Users projected savings
print(f"Projected savings after one year, with interest, is: {projected_savings}")