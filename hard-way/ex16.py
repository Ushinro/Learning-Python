from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# The 'w' parameter will open the file for write access
# 'w' (write) truncates an existing file
# 'a' (append) appends to the end of an existing file
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# .truncate() will empty the given file
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# .write() will append a string to the end of the file.
# Spaces and newlines must be added manually at the end of a line.
target.write("%s\n%s\n%s" % (line1, line2, line3))
# The following lines will produce the same as above
# target.write("""%s
# %s
# %s
# """ % (
# line1, line2, line3))

print("And finally, we close it.")
target.close()
