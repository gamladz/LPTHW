# from the system package import the argv feature
from sys import argv


# expect two variables to be assignes, script an filename
script, filename = argv

# txt is a function which opens the filename
txt = open(filename)

# print the name of the file inputted by the users
print "Here's your file %r:" % filename

# read the txt function
print txt.read()

print "Type the filename again:"
# expect raw input from user again
file_again = raw_input("> ")


# txt_again is a function which opens the file
txt_again = open(file_again)

print txt_again.read()