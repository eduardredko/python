import sys

digit_string = sys.argv[1]

length = len(digit_string)

a = 0

for i in range(length):
    b = int(digit_string[i:i+1])
    a = a + b

print(a)