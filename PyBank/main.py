#Import the os modules
import os

#Module for reading CSV files.
import csv
#Module for statistics functions
import statistics

#Function to count the amount of months in the CSV file.
def Count_Months_Budget (months):
 i=0

     #Loop through data
 for row in months:
            titlecase=row[0].title() #All the months are put in title format.
            i=i+1 #This counter helps us to know how many months

 return i

#Fuction tu calculate the total profits. It uses an accumulating algorithm.
def Profit_Losses_Total(profits):
 accumulated=0
 
 for number in profits:
        accumulated=accumulated+int(number)
      
 return accumulated

#In this function, it substracts the current value and the previous one.
def Changes(profits):
 average=[]
 calculation=0
 i=-1 #It starts in -1 because we do not want to take into account the first element. This is due to the substract made in the for loop.

 for index,number in enumerate(profits): #The index gives access to the position of the values in order to make calulations with the previous value of the
        calculation=int(profits[index])-int(profits[index-1])
        average.append(calculation)
 #In case, it is necessary to start the for loop in a value that is not zero, the syntaxis is the following: enumerate(profits[2:])
 
 return average[1:]

csvpath = os.path.join('Week 3 - Python_Homework_PyBank_Resources_budget_data.csv')

months=[]
profits=[]
average_chane=[]


with open(csvpath, 'r') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader,None) #This line is used to skip the header. Otherwise, it will be counted as pat of the months in the file.
    

    for row in csvreader:
        # Add list months
        months.append(row[0])

        # Add list profits
        profits.append(row[1])

  
    amount_months=Count_Months_Budget (months)
    total_profits=Profit_Losses_Total(profits)
    average_change=Changes(profits)
    final_average_change=round(statistics.mean(average_change),2)
    index_min=average_change.index(min(average_change)) #With this instruction, the index for the minimun value is obtained.
    index_max=average_change.index(max(average_change)) #With this instruction, the index for the maximum value is obtained.
    minimum_value=min(average_change)
    minimum_date=months[index_min+1]
    maximum_value=max(average_change)
    maximum_date=months[index_max+1]

print("Financial Analysis\n","----------------------------")
print(f"Total Months: {amount_months}")
print(f"Total: ${total_profits}")
print(f"Average changes: ${final_average_change}") #In this line it calculates automatically the mean of the processed list.
print (f"Greatest Increase in Profits: {maximum_date} (${maximum_value})")
print (f"Greatest Decrease in Profits: {minimum_date} (${minimum_value})")

#All the results are put together in a list.
cleaned_txt =["Financial Analysis\n","----------------------------\n","Total Months: "+ str(amount_months)+"\n", "Total: $"+str(total_profits)+"\n","Average changes: $"+str(final_average_change)+"\n","Greatest Increase in Profits: " +str(maximum_date)+" $"+ str(maximum_value)+"\n","Greatest Decrease in Profits: "+str(minimum_date) +" $"+ str(minimum_value)]

#Saving a new txt file with the results.

file1 = open("results_bugdet_data.txt","w")

file1.writelines(cleaned_txt)

file1.close()


