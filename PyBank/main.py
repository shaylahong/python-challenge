# dependencies
import os
import csv

# path to dataset 
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")
 
# read csv file and analyse data 
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
    
    # changes in profit and losses & average 
    change = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]
    average_change = sum(change)/len(change)
    
    # greatest increase/decrease in profit 
    greatest_increase = max(change)
    greatest_decrease = min(change)
    greatest_increase_date = months[change.index(greatest_increase)+1]
    greatest_decrease_date = months[change.index(greatest_decrease)+1]
    
    #print to terminal 
    print("Financial Analysis")
    print("-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Net Total Amount: ${net_profit_losses}")
    print(f"Average Change: ${average_change: .2f}")
    print(f"Greatest Profit Increase: {greatest_increase_date}(${greatest_increase})")
    print(f"Greatest Profit Decrease: {greatest_decrease_date}(${greatest_decrease})")
    
    # export to text file 
    file_to_output = os.path.join("PyBank", "Analysis", "PyBank_Results.txt")
    with open(file_to_output, "w") as txt_file:
        txt_file.write("Financial Analysis\n")
        txt_file.write("-------------------------\n")
        txt_file.write(f"Total Months: {total_months}\n")
        txt_file.write(f"Net Total Amount: ${net_profit_losses}\n")
        txt_file.write(f"Average Change: ${average_change: .2f}\n")
        txt_file.write(f"Greatest Profit Increase: {greatest_increase_date}(${greatest_increase})\n")
        txt_file.write(f"Greatest Profit Decrease: {greatest_decrease_date}(${greatest_decrease})\n")