#The data we need to retrieve / add our dependencies
import csv
import os

#Assign a variable for the file to load from a the path
file_to_load = os.path.join("Resources", "election_results.csv")

#create a filename variable to save to a direct or indirect path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total votes counter variable
total_votes = 0

#declare a new list
candidate_options = []

#declare a dictionary to hold names(keys) and votes (values)
candidate_votes = {}

#winning candidate and winning count tracker
#declare empty string variable for winning candidate
winning_candidate = ""

#declare winning count and percentage = 0
winning_count = 0
winning_percentage = 0

#open election results and read file, election_data is the filename object
with open(file_to_load) as election_data:

    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in (file_reader):
        #increment the total votes by 1
        total_votes += 1   
        
        #print the candidate name from each row
        candidate_name = row[2] 

        if candidate_name  not in candidate_options:

            #add the candidate name to the candidate list if not there already
            candidate_options.append(candidate_name)

            #begin tracking that candidate's votes
            candidate_votes[candidate_name] = 0

        #add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#save the results to text file 
with open(file_to_save, "w") as txt_file:

    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes: ,}\n"
        f"------------------------\n")    
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)

    #iterate through candidate_options[] (thru the candidate list)
    for candidate_name in candidate_votes:

        #retrieve the votes for the candidate from the dictionary
        votes = candidate_votes[candidate_name]

        #calculate the percentage of the vote count
        vote_percentage = float(votes) / float(total_votes) * 100

        #print each candidates name, vote count and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        #print each candidates name, vote count and percentage of votes
        #print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if thrue then set winning vales
            winning_count = votes
            winning_percentage = vote_percentage
            #and winning candidate name
            winning_candidate = candidate_name

    #winning candidate summary
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count: ,}\n"
        f"Winning Percentaeg: {winning_percentage: .1f}\n"
        f"----------------------------\n")

    print(winning_candidate_summary)
    #save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

        
           # f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n"
          #  f"------------------------\n"
          #  f"Winner: {winning_candidate}\n"
         #   f"Winning Vote Count: {winning_count: ,}\n"
        #    f"Winning Percentaeg: {winning_percentage: .1f}\n"
         #   f"----------------------------\n")
            
        
      #  txt_file.write(Election_Results)

      
  




