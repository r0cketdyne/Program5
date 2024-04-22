#Matthew Stephenson
#04/20/2024
#Program 5
#this prog reads a list of grades, computes the average grade, the median grade, the high and low
#grades, and print a histogram where each * represents one of the counted grade types.
#################################################################################################


#For this program, you will read a set of numbers and store them in a list. For example, the list of
#numbers represents a set of test grades. You may read the numbers in from the keyboard (as shown in
#the sample below OR you may prompt the user to open a file that contains the numbers. The data
#values should be one per line.
#Read in the numbers and save them in a list. (Hint: append is useful here).
#Also, create a second list that stores a set of counter values. The first element is the count of grades >=
#90 (the A’s), the second element stores the count of grades >= 80 (the B’s), and so on. Do not use
#individual counters. Store the counts in a 5 element list.
#After you have read the list of grades, compute the average grade, the median grade, the high and low
#grades, and print a histogram where each * represents one of the counted grade types

setnum = input("we will likely just prompt the user for something instead of passing in a file. initial commit")

print(setnum)