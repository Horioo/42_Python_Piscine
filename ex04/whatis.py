import sys

argc = len(sys.argv)

if argc == 1:
	sys.exit(0)

assert argc == 2, "more than one argument is provided"

try:
	arg = int(sys.argv[1])
except ValueError:
	raise AssertionError("argument is not an integer") from None

if arg % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")