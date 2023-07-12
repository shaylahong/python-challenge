import os
import csv 

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    election_data_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(election_data_reader)
    print(f"CSV Header: {csv_header}")

# dataset is composed of: "Ballot ID", "County", "Candidate" columns 
#total votes

    total_votes = 0
    candidate_list = []
    for row in election_data_reader:
        total_votes += 1 
        #candidates received votes
        candidate = row[2]
        if candidate not in candidate_list:
            candidate_list.append(candidate)
    print("Total Votes: ", total_votes)
    for candidate in candidate_list:
        print(candidate) 
    
