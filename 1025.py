import sys

numbers = []
line = sys.stdin.readline()
line = sys.stdin.readline()
for n in line.split():
    numbers.append(int(n))
numbers.sort()

votes = 0
for g in numbers[0:int(len(numbers)/2) + len(numbers) % 2]:
    votes += int(g / 2) + 1
print(votes)
