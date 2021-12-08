import sys

line = sys.stdin.readline()
result = 2
for n in line.split():
    result *= int(n)
print(result)
