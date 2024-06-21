def main():
    """
    This function contains the main logic of the program.
    """
    incomes = []
    num_months = int(input("How many months? "))
    for month in range(1, num_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """
    This function prints the income report with cumulative totals.
    param incomes: A list of monthly incomes
    """
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


if __name__ == "__main__":
    main()