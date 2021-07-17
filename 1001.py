import sys, math

numbers = []
for line in sys.stdin.readlines():
    for n in line.split():
        numbers.append(int(n))
numbers.reverse()
for n in numbers:
    print(format(math.sqrt(n),'.4f'))
