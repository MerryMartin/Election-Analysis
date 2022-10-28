#The data we need to retrieve
import csv
import os


#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#create a filename variable to save to a direct or indirect path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open election results and read file, election_data is the filename object
with open(file_to_load) as election_data:

    #to do: read and analyze the date with variable file_reader
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    print(headers)


    #print each row in the csv file
    #for row in file_reader:
     #   print(row)


#Close the file
#election_data.close()  -not using this b/c we're using with

#use the open statement to open the file as a text file w/ filename variable outfile
with open(file_to_save, "w") as txt_file:
    #write some data to the file
    txt_file.write("Counties in the Election\n\nArapahoe\nDenver\nJefferson")
  

#close the file
#outfile.close()

#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

