#-----------------------------------------------#
#                                               #
#  All the rights reserved for 'MD SERAJ KHAN'  #
#       https://www.github.com/seraj48522       #
#                                               #
#-----------------------------------------------#

# Program to Display The Fibonacci series
print("Program to Dispaly Fubonacci Series >>>")

# Taking Input from user to get Length of Series
length = int(input("Enter Length of Series : "))

# Initialise the first two numbers & print here
n1, n2 = 0, 1
print(n1, "\t", n2, "\t", end = "")

# Loop to display the rest of the elements of the Series
for i in range(0, length):
    # Swapping the Number's
    n1, n2 = n2, n1 + n2
    print((n1 + n2), "\t", end = "")