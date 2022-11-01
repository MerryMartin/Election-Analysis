# Election-Audit-Analysis

## Project Overview
A friend at the Colorado board of elections has asked me to help audit the tabulated results for a recent US Congressional election.  His hope is that I can help develop a method to audit the results with Python, instead of Excel, so that he can utilize the new method to analyze different elections in the future.  

## Resources
Analysis was done with the following resources:
Data Source:  election_results.csv
Software:  Python version 3.9.12, Visual Studio Code version 1.72.0

## Summary
The analysis of the election audit was begun by using dependencies and then joining files.  Lists and dictionaries were used to organize the data so it could be analyzed in loops, with membership operators.  

![lists_and_dictionaries](https://user-images.githubusercontent.com/115426070/199115408-5de60ebc-d8af-4be5-bdd8-18ef4a8b7aff.png)

The audit conclusions were then organized in f-strings so they could be neatly presented in both the terminal and text file used by the election committee.  

![fstring_and_text_file](https://user-images.githubusercontent.com/115426070/199115744-317b9da0-ba24-4b17-8729-1390ea9cb650.png)

### Overview of Election Audit Results
* The total votes cast in the congressional election was 369,711.
* The turnout for each county (both percent of the total votes and total number of votes cast) is best illustrated from the text file below:
 
![County_breakdown](https://user-images.githubusercontent.com/115426070/199116381-cc44d62c-9a8b-461d-b753-d379eb7fb76c.png)

* Denver County had the largest turnout, with 306,055 votes cast.
* Diana DeGette won the popular election, with Charles Casper Stockham coming in second place and Raymon Anthony Doane coming in third place.  The compiled results for each candidate (both percent of the total votes cast and total number of votes received) are below:

![candidate_results](https://user-images.githubusercontent.com/115426070/199117189-9278d0b6-fd95-46ae-bb10-9eea3f0680f6.png)

* Diana DeGette won with this election with 73.8% of the votes cast for her, a total of 272,892 votes.  

![winner](https://user-images.githubusercontent.com/115426070/199118328-113f0183-4adf-4a9b-b199-9449cf50a8ab.png)

### Election Audit Summary
My proposal to the election commission on how this script can be modified and used for any future elections are as follows.  
* Since lists and dictionaries were used for this audit, this script can be scaled up to elections that have many more candidates or participating counties.  Additional lists could also be created if the election commmission wanted to analyze more criteria, like how many votes in the counties went to each political party.   
* Turnout could be further analyzed by adding voter registration data to see how many registered voters particiapted in the election and which counties they represented.  


