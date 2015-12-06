from sys import argv

script, filename = argv

# Takes the filename arguments and tells user its is liable to deletion
print "We're going to erase %r." % filename
print "if you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")
#Takes input of RETURN or CTRL-C to determine the users next action

print "Opening the file..."

# target is a variable which opens the filename in writable formati
target = open(filename, 'w')

# Truncate empties the target variable, not actually necessary as the file
# is opened in writable format, so when you begin writing you will automatically overlap
print "truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."
# Assignes raw string input from users into 3 different variables, line 1, line 2, line 3
line1 = raw_input ("line 1: ")
line2 = raw_input ("line 2: ")
line3 = raw_input ("line 3: ")

print "I'm going to write these to the file"

# Writes line1, line2 and line3 to the file
target.write(line1, "\n",  line2, "\n",  line3)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n") 

print "And finally we close it"
target.close()