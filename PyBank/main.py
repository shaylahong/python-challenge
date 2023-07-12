import os
import csv

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    budget_data_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(budget_data_reader)

# dataset composed of: "Date" & "Profit/Losses" columns
    months = []
    profit_losses = []

    for row in budget_data_reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
    # total number of months 
        total_months = len(months)
    
   # net total amount 
    net_profit_losses = sum(profit_losses)
    
    #changes in profit and losses & average 
    change = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]
    average_change = sum(change)/len(change)
    
    # greatest increase/decrease in profit 
    greatest_increase = max(change)
    greatest_decrease = min(change)
    greatest_increase_date = months[change.index(greatest_increase)+1]
    greatest_decrease_date = months[change.index(greatest_decrease)+1]
    
    print("Financial Analysis")
    print(f"Total Months: {total_months}")
    print(f"Net Total Amount: ${net_profit_losses}")
    print(f"Average Change: ${average_change: .2f}")
    print(f"Greatest Profit Increase: {greatest_increase_date}(${greatest_increase})")
    print(f"Greatest Profit Decrease: {greatest_decrease_date}(${greatest_decrease})")
    