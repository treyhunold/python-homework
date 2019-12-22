from pathlib import Path
import csv

budget_data_path = Path("../Resources/budget_data.csv")

count_net = 0
total_months = 0
month = []
delta_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(budget_data_path, "r") as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months = total_months + 1
    count_net = count_net + int(first_row[1])
    count_prev = int(first_row[1])
    
    for row in csvreader:
        total_months = total_months + 1
        count_net = count_net + int(row[1])
        delta = int(row[1]) - count_prev
        count_prev = int(row[1])
        delta_list = delta_list + [delta]
        month = month + [row[0]]
        if delta > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = delta
        if delta < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = delta
            
monthly_avg = round(sum(delta_list) / len(delta_list),2)

financial_analysis_path = Path("analysis/financial_analysis.txt")

with open(financial_analysis_path, "w") as txt_file:
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${count_net}\n")
    txt_file.write(f"Average  Change: ${monthly_avg}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")