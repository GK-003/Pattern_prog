i = 1
while i <= 5:
  print('*' * i)
  i = i+1

for i in range(4,0,-1):
  for j in range(i):
    print('*', end="")
  print("")
