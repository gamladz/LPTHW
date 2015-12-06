name = 'Gameli Y. Ladzekpo'
age = 22 # not a lie
height = 73 #inches
weight = 200 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

#convert imperial units to metric units
cm_height = 2.54*height
kg_weight = 0.45*weight 


print "Let's talk about %s." %name
print "He's %d inches tall." %height
print "That's %d cm" %cm_height
print "He's %d pounds heavy." %weight
print "That's %d kgs" %kg_weight 
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

# this line is tricky, try to get it exactly right
print "If i add %d, %d, and %d i get %d. " % (age, height, weight, age + height + weight)
