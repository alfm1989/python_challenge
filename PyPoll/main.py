#Import the os modules
import os

#Module for reading CSV files.
import csv
#Module for statistics functions
import statistics

#Function to count the amount of total votes in CSV file.
def Count_Votes (vote_id):
 i=0

     #Loop through data
 for row in vote_id:
           i=i+1 #This counter helps us to know how many months

 return i

#Fuction to calculate de amount of votes per candidate.
def Votes_Per_Candidate(candidate):
 candidate_accumulated=[0,0,0,0]
 
 for person in candidate:
        if person=="Khan":
            candidate_accumulated[0]+=1
        else:
            if person=="Correy":
                candidate_accumulated[1]+=1
            else:
                if person=="Li":
                    candidate_accumulated[2]+=1
                else:
                    if person=="O'Tooley":
                        candidate_accumulated[3]+=1

      
 return candidate_accumulated



csvpath = os.path.join('Week 3 - Python_Homework_PyPoll_Resources_election_data.csv')

vote_id=[]
county=[]
candidate=[]
candidates_name=["Khan","Correy","Li","O'Tooley"]
candidate_voting=[]
percentages=[]

with open(csvpath, 'r') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader,None) #This line is used to skip the header. Otherwise, it will be counted as pat of the months in the file.
    

    for row in csvreader:
        # Add list Vote ID
        vote_id.append(row[0])

        # Add county
        county.append(row[1])

        # Add candidate
        candidate.append(row[2])

    
#Print results
amount_votes=Count_Votes (vote_id)
print("Election Results\n--------------------")
print(f'Total Votes: {amount_votes}\n--------------------')
candidate_voting=Votes_Per_Candidate(candidate)   

# Loop through the candidate_voting list
for candidate_index in range(len(candidate_voting)):
    candidate_count = (candidate_voting[candidate_index])#This variable takes the candidate vote counting for each one.
    candidate_name = str(candidates_name[candidate_index]) #This variable takes the candidate name for printing it according to their vote counting.
    percentages.append(round(((candidate_count/amount_votes)*100),2)) #This is the list that has de percentages for each candidate.

    # Gather the count of each candidate in the candidate list and print them alongside the candidate's name
    print (f"{candidate_name}: {round(((candidate_count/amount_votes)*100))}% ({candidate_count})")

print("--------------------")
index_max=candidate_voting.index(max(candidate_voting)) #With this instruction, it is taken the index for the maximum votes gotten.
maximum_value=max(candidate_voting)

print(f"Winner: {candidates_name[index_max]} with {maximum_value} votes")


#All the results are put together in a list.
cleaned_txt =["Election Results\n","----------------------------\n","Total Votes: "+ str(amount_votes)+"\n","----------------------------\n",\
 str(candidates_name[0])+": "+str(percentages[0])+"% "+str(candidate_voting[0])+"\n",\
 str(candidates_name[1])+": "+str(percentages[1])+"% "+str(candidate_voting[1])+"\n",\
 str(candidates_name[2])+": "+str(percentages[2])+"% "+str(candidate_voting[2])+"\n",\
 str(candidates_name[3])+": "+str(percentages[3])+"% "+str(candidate_voting[3])+"\n",\
 "----------------------------\n",\
 "Winner: "+str(candidates_name[index_max])]

#Saving a new txt file with the results.

file1 = open("results_election_data.txt","w")

file1.writelines(cleaned_txt)

file1.close()


