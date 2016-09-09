# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). 

#Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

with open('football.csv', 'r') as csvfile:
    football = (csv.reader(csvfile))
    next(football)
    values = [abs(int(row[5])-int(row[6])) for row in football]
    min_value_index = values.index(min(values))
    teams = [row[0] for row in football]
    print teams[min_value_index]
