#import dependencies 
import os 
import csv

#set path 
poll_path = os.path.join("election_data.csv")

#output path 
file_output = ("election_data.txt")

# set variables
total_votes = 0
candidates = []
poll = []
candidate_votes = []
candidate_percent = []
winner = ""

#open file
with open(poll_path, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   header = next(csvreader)

#loop
   for row in csvreader:
       total_votes = total_votes + 1
       candidate = row[2]
       if candidate in candidates:
           candidate_index = candidates.index(candidate)
           candidate_votes[candidate_index] = candidate_votes[candidate_index] + 1
       else:
           candidates.append(candidate)
           candidate_votes.append(1)

#percentage
max_count=0
for count in range(len(candidate_votes)):
   percent = "{:.3%}".format((candidate_votes[count]/total_votes))
   candidate_percent.append(percent)
   if candidate_votes[count]>total_votes:
       total_votes=candidate_votes[count]
       max_count = count

#winner is 
popular_vote = candidate_votes.index(max(candidate_votes))
winner = candidates[max_count]

# print 
print("Election Results:")
print("------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------")
for count in range(len(candidates)):
   print(f"{candidates[count]} : {candidate_percent[count]} ({candidate_votes[count]})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")


 #print to txt file
with open(file_output,'w') as txtfile:
   txtfile.write(f"Election Results:\n")
   txtfile.write(f"---------------------------\n")
   txtfile.write(f"Total Votes:{total_votes}\n")
   txtfile.write("------------------------")
   for count in range(len(candidates)):
      txtfile.write(f"{candidates[count]} : {candidate_percent[count]} ({candidate_votes[count]})\n")
   txtfile.write("------------------------\n")
   txtfile.write(f"Winner: {winner}\n")