from itertools import product #중복허용

n = int(input()) # 5

time = [ i for i in range(n+1)]
minutes = [ k for k in range(60)]
seconds = [ k for k in range(60)]

three = [3,13,23,33,43,53]

cnt = 0

for i in time:
  for z in minutes:
    for k in seconds:
      if(time[i] in three or minutes[z] in three or seconds[k] in three):
        cnt += 1

print(cnt)
