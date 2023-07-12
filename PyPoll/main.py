# dependencies 
import os
import csv 

# path to dataset
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

# read csv file and analyse data 
with open(election_data) as csvfile:
    election_data_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(election_data_reader)

# dataset is composed of: "Ballot ID", "County", "Candidate" columns 

    total_votes = 0
    candidate_votes = {}
    for row in election_data_reader:
        # total votes 
        total_votes += 1 
        #candidates received votes
        candidate = row[2]
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 1 
        else:
            candidate_votes[candidate] += 1 

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# percentage votes each candidate won & total number of votes 
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage: .3f}% ({votes})")

    print("-------------------------")

#winner of election based on popular vote 
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")

# export to text file 
file_to_output = os.path.join("PyPoll", "Analysis", "PyPoll_Results.txt")
with open(file_to_output, "w") as txt_file:
     txt_file.write("Election Results\n")
     txt_file.write("-------------------------\n")
     txt_file.write(f"Total Votes: {total_votes}\n")
     txt_file.write("-------------------------\n")

     for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        txt_file.write(f"{candidate}: {percentage: .3f}% ({votes})\n")
     
     txt_file.write("-------------------------\n")
     txt_file.write(f"Winner: {winner}\n")
     txt_file.write("-------------------------\n")