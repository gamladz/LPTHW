from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

# indata opens the contents of from_file and then reads it
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

# Checks if output file exists or whether it needs to be created
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to contine, CTRL-C to abort"
raw_input()

#out_file is opened as a writable file and then the variable indata is written to it.
# No need to close the file as the file automatically closes after the opem command is written to it, garbage-collection but not best practice

out_file = open(to_file, 'w').write(indata)

print "Alright, all done."


