# %d inserts a digit (int) into the string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# Insertion of variables in respective order
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

# Prints the raw data of x
print("I said: %r." % x)
print("I also said: '%s'." %y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# The string variable can have the format character inserted later
# This allows for reuse
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

# String concatenation
print(w + e)
