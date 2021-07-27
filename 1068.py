import sys
for n in sys.stdin.readlines():
    n = int(n)
    if n >= 1:
        print(sum(range(1, n + 1)))
    else:
        print(sum(range(n, 2)))

