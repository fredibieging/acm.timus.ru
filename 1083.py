n = [len(x) if "!" in x else int(x) for x in input().split(' ')]
answer = 1
for x in range(n[0], 1, n[1] * -1):
  answer *= x
print(answer)
