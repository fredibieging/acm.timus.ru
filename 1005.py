import sys, math

sys.stdin.readline()
n = [int(x) for x in input().split(' ')]
total = sum(n)

def find_min(i, calculated):
    if (i == 0):
        return abs((total - calculated) - calculated)
    return min(find_min(i - 1, calculated + n[i - 1]), find_min(i - 1, calculated))

answer = find_min(len(n), 0)
print(answer)
