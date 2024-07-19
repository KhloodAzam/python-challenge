import csv
import os 

with open('python-challenge/Pybank/Resources/budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  


    months = []
    ploss = []
    plchange= []

    for row in reader:
        months.append(row[0])
        ploss.append(int(row[1]))

print("Financial Analysis")

print("-----------------------------")

total_months = len(months)
print(f"Total Months: {total_months}")

net_total = sum(ploss)

print(f"Total: ${net_total}")


for i in range(1, total_months):
    change = ploss[i] - ploss[i-1]
    plchange.append(change)


average_change = sum(plchange) / len(plchange)

print(f"Average Change: ${average_change:.2f}")

greatest_increase = max(plchange)


greatest_increase_date = months[plchange.index(greatest_increase) + 1]

print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
greatest_decrease = min(plchange)
greatest_decrease_date = months[plchange.index(greatest_decrease) + 1]
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")




with open('financial_analysis.txt', 'w') as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-----------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_total}\n")
    text_file.write(f"Average Change: ${average_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
