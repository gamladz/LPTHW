#State how many people there are in the world
x = "THere are `%d types of people." % 10

#Give variables string values 
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#parses hilarious value into joke evaluation variable 
print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e 