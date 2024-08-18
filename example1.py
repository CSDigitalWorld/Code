# Function to get the user's monthly budget
def input_budget():
    while True:  # Loop to keep asking for input until a valid number is entered
        try:
            budget = float(input("Enter your monthly budget: "))  # Try converting the input to a float
            return budget  # Return the valid budget
        except ValueError:  # If conversion fails (input is not a number), catch the error
            print("Please enter a valid number for the budget.")  # Prompt the user to enter a valid number

# Function to get the list of expenses from the user
def input_expenses():
    expenses = []  # Initialize an empty list to store expenses
    while True:  # Loop to keep asking for expenses until the user is done
        expense = input("Enter an expense (or type 'done' to finish): ")  # Prompt the user for an expense
        if expense.lower() == 'done':  # Check if the user typed 'done' (case-insensitive)
            break  # Exit the loop if the user is done entering expenses
        try:
            expense_value = float(expense)  # Try converting the input to a float
            expenses.append(expense_value)  # Add the valid expense to the list
        except ValueError:  # If conversion fails (input is not a number), catch the error
            print("Please enter a valid number for the expense.")  # Prompt the user to enter a valid number
    return expenses  # Return the list of expenses

# Function to calculate the total of all entered expenses
def calculate_total_expenses(expenses):
    return sum(expenses)  # Sum up all the numbers in the expenses list and return the total

# Function to compare the total expenses with the budget and give feedback
def compare_expenses_to_budget(budget, total_expenses):
    if total_expenses > budget:  # Check if the total expenses exceed the budget
        print("You are over your budget by ${:.2f}.".format(total_expenses - budget))  # Print how much over budget
    else:  # If total expenses are within the budget
        print("You are within your budget by ${:.2f}.".format(budget - total_expenses))  # Print how much under budget

# Main function that orchestrates the budget tracking process
def main():
    budget = input_budget()  # Step 1: Get the budget from the user
    expenses = input_expenses()  # Step 2: Get the list of expenses from the user
    total_expenses = calculate_total_expenses(expenses)  # Step 3: Calculate the total of all expenses
    compare_expenses_to_budget(budget, total_expenses)  # Step 4: Compare the total expenses to the budget

# Entry point of the program
if __name__ == "_main_":
    main()  # Run the main function when the script is executed