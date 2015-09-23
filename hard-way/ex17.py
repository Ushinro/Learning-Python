from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

# Like this! This will not need to run in_file.close()
# indata = open(from_file).read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("All right, all done.")

out_file.close()
in_file.close()

# One-line challenge, but bad practice
# open(to_file, 'w').write(open(from_file).read())
