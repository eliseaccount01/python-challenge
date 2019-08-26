#import dependencies
import os
import csv

#creating a path 
path = os.path.join("budget_data.csv")

#output path 
file_output = ("budget_data.txt")

#open csv 
with open(path,'r') as file:
    csvreader = csv.reader(file,delimiter = ",")
    row = next(csvreader)

#set variables
    total = 0
    previous = 0 
    avg_change = 0 
    net_change =[]
    pnl = []
    months= []
    revenue = 0 
    loss = 0 

#read through rows
    for row in csvreader: 

        #count total 
        total = total + int(row[1])

        # append months and pnl to list 
        months.append(row[0])
        pnl.append(int(row[1]))

        #find monthly change and add to net change
        change = int(row[1]) - previous 

        #add changes to net_change's empty list
        net_change.append(int(change))

        # set current row as previous
        previous = int(row[1])

    #find max and min values
    revenue= max(net_change)
    loss = min(net_change)

    #find max and min months 
    revenue_month = pnl.index(max(pnl))
    loss_month = pnl.index(min(pnl)) 

    #the first month has no net change, removed for accurate avg calculation
    net_change.remove(net_change[0])
    
    #find average change 
    avg_change = float("{0: .2f}".format(sum(net_change)/len(months)))


print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total}")
print(f"Average Change: $ {avg_change}")
print(f"Greatest Increase in Profits: {months[revenue_month]} ${revenue}")
print(f"Greatest Decrease in Profits: {months[loss_month]} ${loss}")

 #print to txt file
with open(file_output,'w') as txtfile:
   txtfile.write(f"Finacial Analysis:\n")
   txtfile.write(f"---------------------------\n")
   txtfile.write(f"Total Months: {len(months)}\n")
   txtfile.write(f"Total: ${total}\n")
   txtfile.write(f"Average Change: $ {avg_change}\n")
   txtfile.write(f"Greatest Increase in Profits: {months[revenue_month]} ${revenue}\n")
   txtfile.write(f"Greatest Decrease in Profits: {months[loss_month]} ${loss}\n")