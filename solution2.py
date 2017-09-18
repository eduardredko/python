import sys

digit_string = sys.argv[1]
numb = int(digit_string)

for i in range(numb + 1):
    print(" "*(numb - i) + "#"*i)
