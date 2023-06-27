import os
import csv

# Open the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath) as csvfile:
    # Create Reader Object for the CSV
    csvreader = csv.reader(csvfile)
    next(csvreader)

    # Set the output text file path
    output_log_path = "PyBank_analysis.txt"

    # Set variables
    total_months = 0
    total_profit_losses = 0
    profit_losses = []
    previous_profit_losses = 0
    month_of_change = []
    profit_losses_change_list = []
    greatest_decrease = ["", 9999999]
    greatest_increase = ["", 0]

    # Loop through rows to calculate metrics
    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the total profit_losses over the entire period
        total_profit_losses += int(row[1])

        # Calculate the change in profit_losses between months
        profit_losses_change = int(row[1]) - previous_profit_losses
        previous_profit_losses = int(row[1])
        profit_losses_change_list.append(profit_losses_change)
        month_of_change.append(row[0])

        # Find the greatest increase in profit_losses (date and amount) over the entire period
        if profit_losses_change > greatest_increase[1]:
            greatest_increase[1] = profit_losses_change
            greatest_increase[0] = row[0]

        # Find the greatest decrease in profit_losses (date and amount) over the entire period
        if profit_losses_change < greatest_decrease[1]:
            greatest_decrease[1] = profit_losses_change
            greatest_decrease[0] = row[0]

    # Calculate the average change in profit_losses between months over the entire period
    profit_losses_average = sum(profit_losses_change_list) / len(profit_losses_change_list)

    # Print the analysis results
    print("Financial Analysis")
    print("---------------------")
    print("Total Months:  %d" % total_months)
    print("Total: $%d" % total_profit_losses)
    print("Average Change: $%.2f" % profit_losses_average)
    print("Greatest Increase in Profits: %s ($%d)" % (greatest_increase[0], greatest_increase[1]))
    print("Greatest Decrease in Profits: %s ($%d)" % (greatest_decrease[0], greatest_decrease[1]))

    # Write the analysis results to the output text file
    with open(output_log_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("---------------------\n")
        file.write("Total Months: %d\n" % total_months)
        file.write("Total: $%d\n" % total_profit_losses)
        file.write("Average Change: $%.2f\n" % profit_losses_average)
        file.write("Greatest Increase in Profits: %s ($%d)\n" % (greatest_increase[0], greatest_increase[1]))
        file.write("Greatest Decrease in Profits: %s ($%d)\n" % (greatest_decrease[0], greatest_decrease[1]))
