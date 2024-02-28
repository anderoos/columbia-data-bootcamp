import csv 
import time

def pybank_analyzer(dict_reader_obj):
    budget_data_as_list = list(dict_reader_obj)
    total_profits = 0
    running_deltas = []
    # Capture length of budget_data
    total_months = len(budget_data_as_list)
    # Store header labels
    col_labels = budget_data_as_list[0].keys()
    # Loop through rows
    for row_num in range(len(budget_data_as_list)):
        # Added if statement to skip zero index. Otherwise would subtract from last value from list
        if row_num == 0:
            total_profits += int(budget_data_as_list[row_num]['Profit/Losses'])
            running_deltas.append(0)
        else:
            # Calculate total profits by iterating through list
            total_profits += int(budget_data_as_list[row_num]['Profit/Losses'])
            # Calculate differences in profits between months
            running_deltas.append(int(budget_data_as_list[row_num]['Profit/Losses']) - int(budget_data_as_list[row_num - 1]['Profit/Losses']))
            # Capture greatest loss
            max_loss = min(running_deltas)
            # Capture greatest gains
            max_gains = max(running_deltas)
            # Capture index of max_gains and max_loss and take string from Date column
            max_loss_date = budget_data_as_list[running_deltas.index(max_loss)]['Date']
            max_gains_date = budget_data_as_list[running_deltas.index(max_gains)]['Date']
    # Calculate changing average
    average_change = round(sum(running_deltas)/ (total_months-1), 2) 
    # Print results
    print(f"""Financial Analysis
    ----------------------------
    Total Months: {total_months}
    Total: ${total_profits}
    Average Change: ${average_change}
    Greatest Increase in Profits: {max_gains_date} (${max_gains})
    Greatest Decrease in Profits: {max_loss_date} (${max_loss})
    """)
    # Export as txt
    export_status = input("Export as .txt file? ")
    if export_status == "Yes":
        print("Exporting...\n")
        time.sleep(1)
        with open('Pybank/analysis/results.txt', "w") as export:
            export.write(f"""
                        Financial Analysis
                        ----------------------------
                        Total Months: {total_months}
                        Total: ${total_profits}
                        Average Change: ${average_change}
                        Greatest Increase in Profits: {max_gains_date} (${max_gains})
                        Greatest Decrease in Profits: {max_loss_date} (${max_loss})
                        """)
        
        
# Function execution
with open("Pybank/Resources/budget_data.csv", newline="") as budget_data_csv:
    budget_data_dict_reader = csv.DictReader(budget_data_csv)
    pybank_analyzer(budget_data_dict_reader)
