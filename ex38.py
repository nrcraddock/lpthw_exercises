ten_things = "apples oranges crows telephone light sugar"

print "Wait, there's not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') #this splits the string variable above into a list.
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Laser Gun", "Ostrich", "Balalaika"]
#notice that you define lists with square braces.

while len(stuff) != 10:
	next_one = more_stuff.pop() #pop something off the more stuff list.
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] #prints the second item in the list (in the 1 spot in 0, 1, 2, etc.)
print stuff[-1] #fancy. prints the last item in the list.
print stuff.pop() #pops the last word off the list and prints it.
print ' '.join(stuff) #puts whatever is in the inserted string in between each member of the list.
print '#'.join(stuff[3:5]) #prints a slice of the list with # inserted between, starting at three and stopping before 5. similar to range(3,5)