#!/usr/bin/env python

print "Hello World.  This is my first python script.  Hooray for me.\n"

#in python you can comment out like this

'''Or you can comment out larger sections using 3 commas
on each side of whatever you would like to say
it can also span multiple lines'''

#in python you can directly specify variables like this

variable1 = 'this is so cool'

#or you can have users enter information like this
variable2 = raw_input('Enter your name: ')

#now lets do something with this variable, i.e. string of characters
#now many characters are in this string?, can use the len() function

length = len(variable2)

#Now print out your results
print "\nThere are %i characters in your name (%s)" % (length, variable2)

#you can also print strings like this
print "and btw, " + variable1

